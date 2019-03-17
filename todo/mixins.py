import json

from django.shortcuts import render_to_response
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound
)

class AjaxBaseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(AjaxBaseMixin, self).dispatch(request, *args, **kwargs)
        else:
            return self.http_bad_request('This is endpoint supports only AJAX requests!')

    def http_not_found(self):
        return HttpResponseNotFound()

    def http_bad_request(self, error):
        response_kwargs = {'content_type': 'application/json'}
        return HttpResponseBadRequest(self.serialize_to_json(error), **response_kwargs)

    def response(self, context):
        if (self.template_name):
            return render_to_response(self.template_name, context)

        response_kwargs = {'content_type': 'application/json'}
        return HttpResponse(self.serialize_to_json(context), **response_kwargs)

    def get_context_data(self, context):
        return context

    def serialize_to_json(self, data):
        return json.dumps(data)


class AjaxCreateMixin(AjaxBaseMixin):
    def form_valid(self, form):
        # Save an object
        self.object = form.save()

        # Initialize a context
        context = {self.context_object_name or 'instance': self.object}

        return self.response(self.get_context_data(context))

    def form_invalid(self, form):
        return self.http_bad_request(form.errors)


class AjaxUpdateMixin(AjaxCreateMixin):
    pass


class AjaxDeleteMixin(AjaxBaseMixin):
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object:
            return self.http_not_found()

        # Delete an object
        self.object.delete()

        # Initialize an empty context
        context = {}

        return self.response(self.get_context_data(context))
