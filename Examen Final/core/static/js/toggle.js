    function toggleEdit(showEdit) {
        var profileView = document.getElementById('profile_view');
        var profileEdit = document.getElementById('profile_edit');
        if (showEdit) {
            profileView.style.display = 'none';
            profileEdit.style.display = 'block';
        } else {
            profileView.style.display = 'block';
            profileEdit.style.display = 'none';
        }
    }