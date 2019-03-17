/**
 * Tasks module
 */
$(function() {
	function checkOnEmpty() {
		var count = $('#outstanding_tasks li').size();
		if (count === 0) {
			$('#outstanding_tasks_empty_indicator').remove();
			$('#outstanding_tasks').after("<p id=\"outstanding_tasks_empty_indicator\">List is empty</p>");
		} else {
			$('#outstanding_tasks_empty_indicator').remove();
		}

		count = $('#completed_tasks li').size();
		if (count === 0) {
			$('#completed_tasks_empty_indicator').remove();
			$('#completed_tasks').after("<p id=\"completed_tasks_empty_indicator\">List is empty</p>");
		} else {
			$('#completed_tasks_empty_indicator').remove();
		}
	}

	function applyDoneTaskListeners() {
		$('input[id^="task_is_done_"]').unbind("click").click(function(event) {
			var checkbox = $(this);

			var id = checkbox.data('id');
			var isDone = checkbox.is(':checked');

			doneTask(id, isDone);
		});
	}

	function showErrorAlert(title, message) {
	    $('#error_title').text(title);
	    $('#error_message').text(message);
	    $('#error_alert').show();
	}

	function createTask(description) {
		$.ajax({
			type: 'POST',
			url: '/ajax/tasks/create/',
			data: {
				'description': description
			},
			success: function(html) {
				$('#outstanding_tasks').append(html);
				$('#form_create').trigger('reset');

				// Show empty indicators if it needs
				checkOnEmpty();
				// Apply done task listeners
				applyDoneTaskListeners();
			},
			error: function() {
				showErrorAlert('Error occurred', 'Does not create task. Please try again');
			}
		});
	}

	function editTask(id, description, isDone) {
		if (!id) throw 'task id is requirement';
		$.ajax({
			type: 'POST',
			url: '/ajax/tasks/edit/',
			data: {
				'pk': id,
				'description': description,
				'is_done': isDone
			},
			success: function(html) {
				$('#task_' + id).replaceWith(html);
				// Apply done task listeners
				applyDoneTaskListeners();
			},
			error: function() {
				showErrorAlert('Error occurred', 'Does not update task. Please try again');
			}
		});
	}

	function doneTask(id, isDone) {
		if (!id) throw 'task id is requirement';
		$.ajax({
			type: 'POST',
			url: '/ajax/tasks/done/',
			data: {
				'pk': id,
				'is_done': isDone
			},
			success: function(html) {
			    var task = $('#task_' + id);

				if (isDone) {
					$('#completed_tasks').append(task);
				} else {
					$('#outstanding_tasks').append(task);
				}

				task.replaceWith(html);

				// Show empty indicators if it needs
				checkOnEmpty();
				// Apply done task listeners
				applyDoneTaskListeners();
			},
			error: function() {
			    // Restore the previous task state
			    $('#task_is_done_' + id).attr('checked', !isDone);
			    // Show error alert
				showErrorAlert('Error occurred', 'Does not change task status. Please try again');
			}
		});
	}

	function deleteTask(id) {
		if (!id) throw 'task id is requirement';
		$.ajax({
			type: 'POST',
			url: '/ajax/tasks/delete/',
			data: {
				'pk': id
			},
			success: function() {
				$('#task_' + id).remove();
				// Show empty indicators if it needs
				checkOnEmpty();
			},
			error: function() {
				showErrorAlert('Error occurred', 'Does not delete task. Please try again');
			}
		});
	}

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////s

	// Show empty indicators if it needs
	checkOnEmpty();
	
	// Apply done task listeners
	applyDoneTaskListeners();

    // Apply close alert listener
	$(".close").click(function(){
        $("#error_alert").hide();
    });

	// Create task listener
	$('#form_create').submit(function(event) {
		var description = $('#id_description').val();
		createTask(description);
		return false;
	});

	// Edit task listener
	$('#modal_edit').on('show.bs.modal', function (event) {
  		var button = $(event.relatedTarget); // Button that triggered the modal-edit
  		// Extract info from data-* attributes
  		var id = button.data('id');
  		var description = button.data('description');
  		var isDone = button.data('is-done');

  		var modal = $(this);

  		// Set actual data
  		modal.find('#task_description').val(description);

  		modal.find('.btn-ok').unbind("click").click(function() {
  			// Get updated data
			description = modal.find('#task_description').val();
			editTask(id, description, isDone);
  		});
	});

	// Delete task listener
	$('#modal_delete').on('show.bs.modal', function(event) {
		var button = $(event.relatedTarget); // Button that triggered the modal-delete
  		var id = button.data('id'); // Extract info from data-* attributes
  		
		var modal = $(this);

  		modal.find('.btn-ok').unbind("click").click(function() {
  			deleteTask(id);
  		});
	});
});