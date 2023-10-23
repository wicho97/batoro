
$("#id_date_of_birth").datepicker({
    format: 'yyyy-mm-dd'
});
$("#id_start_date").datepicker({
    format: 'yyyy-mm-dd'
});
$("#id_finish_date").datepicker({
    format: 'yyyy-mm-dd'
});
$("#id_date_of_birth").attr('placeholder', '1990/12/25');
$("#id_start_date").attr('placeholder', '1990/12/25');
$("#id_finish_date").attr('placeholder', '1990/12/25');
$("#id_status").select2();
$("#id_project_manager").select2();
$("#id_client").select2();
$("#id_public").removeClass('c-input');

// Projects

function showAlert(status_id, status_name) {
    Swal.fire({
        title: `Estas seguro de eliminar el estado <u>${status_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/projects/status/delete/' + status_id + '/'
        }
    })
}


function showAlertProject(project_id, project_name) {
    Swal.fire({
        title: `Estas seguro de eliminar el estado <u>${project_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/projects/delete/' + project_id + '/'
        }
    })
}


// Tasks

function showAlertTaskStatus(status_id, status_name) {
    Swal.fire({
        title: `Estas seguro de eliminar el estado <u>${status_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/tasks/status/delete/' + status_id + '/'
        }
    })
}

function showAlertTaskPriority(status_id, status_name) {
    Swal.fire({
        title: `Estas seguro de eliminar la prioridad <u>${status_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/tasks/priority/delete/' + status_id + '/'
        }
    })
}

function showAlertTaskType(status_id, status_name) {
    Swal.fire({
        title: `Estas seguro de eliminar el tipo <u>${status_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/tasks/type/delete/' + status_id + '/'
        }
    })
}
