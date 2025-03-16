<template>
  <div class="profile-cover">
    <div class="profile-cover-wrap">
      <img class="profile-cover-img" src="@/assets/img/profiles/avatar-02.jpg" alt="Profile Cover" />

      <!-- Custom File Cover -->
      <div class="cover-content">
        <div class="custom-file-btn">
          <input type="file" class="custom-file-btn-input" id="cover_upload">
          <label class="custom-file-btn-label btn btn-sm btn-white" for="cover_upload">
            <i class="fas fa-camera"></i>
            <span class="d-none d-sm-inline-block ms-1">Update Cover</span>
          </label>
        </div>
      </div>
      <!-- /Custom File Cover -->
    </div>
  </div>

  <div class="text-center mb-5">
    <label class="avatar avatar-xxl profile-cover-avatar" for="avatar_upload">
      <img class="avatar-img" src="@/assets/img/profiles/avatar-02.jpg" alt="Profile Image" />
      <input type="file" id="avatar_upload" />
      <span class="avatar-edit">
        <i class="feather feather-edit avatar-uploader-icon shadow-soft"></i>
      </span>
    </label>
    <h2>
      Charles Hafner
      <i class="fas fa-certificate text-primary small" data-bs-toggle="tooltip" data-placement="top" title=""
        data-original-title="Verified"></i>
    </h2>
    <ul class="list-inline">
      <li class="list-inline-item">
        <i class="far fa-building"></i> <span>Hafner Pvt Ltd.</span>
      </li>
      <li class="list-inline-item ms-1">
        <i class="fas fa-map-marker-alt"></i> West Virginia, US
      </li>
      <li class="list-inline-item ms-1">
        <i class="far fa-calendar-alt"></i> <span>Joined November 2017</span>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  mounted() {
    if (document.getElementById('blah')) {
      function readURL(input) {
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = function (e) {
            document.getElementById('blah').src = e.target.result;
          };
          reader.readAsDataURL(input.files[0]);
        }
      }

      var avatarUpload = document.getElementById('avatar_upload');
      if (avatarUpload) {
        avatarUpload.addEventListener('change', function () {
          readURL(this);
        });
      }
    }
  },
};
</script>
