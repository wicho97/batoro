let elements_datepicker = [
    "#id_date_of_birth",
    "#id_start_date",
    "#id_finish_date"
];

elements_datepicker.forEach(element => {
    $(element).datepicker({
        format: 'yyyy-mm-dd'
    });
});

let elements_select2 = [
    "#id_status",
    "#id_project_manager",
    "#id_client",
    "#id_priority",
    "#id_type",
    "#id_assigned_to",
    "#id_project"
];

elements_select2.forEach(element => {
    $(element).select2();
});

$("#id_date_of_birth").attr('placeholder', '1990/12/25');
$("#id_start_date").attr('placeholder', '1990/12/25');
$("#id_finish_date").attr('placeholder', '1990/12/25');
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

function showAlertTask(status_id, status_name) {
    Swal.fire({
        title: `Estas seguro de eliminar la tarea <u>${status_name}</u>?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/tasks/delete/' + status_id + '/'
        }
    })
}
