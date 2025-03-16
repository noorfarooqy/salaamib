<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <div class="content-page-header">
          <h5>Edit User</h5>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="card-body">
              <div class="form-group-item">
                <h5 class="form-title">Profile Picture</h5>
                <div class="profile-picture">
                  <div class="upload-profile">
                    <div class="profile-img">
                      <img
                        id="blah"
                        class="avatar"
                        src="@/assets/img/profiles/avatar-10.jpg"
                        alt=""
                      />
                    </div>
                    <div class="add-profile">
                      <h5>Upload a New Photo</h5>
                      <span>Profile-pic.jpg</span>
                    </div>
                  </div>
                  <div class="img-upload">
                    <a class="btn btn-primary me-2">Upload</a>
                    <a class="btn btn-remove">Remove</a>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>First Name</label>
                      <input
                        type="text"
                        class="form-control"
                        value="John"
                        placeholder="Enter First Name"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Last Name</label>
                      <input
                        type="text"
                        class="form-control"
                        value="Smith"
                        placeholder="Enter Last Name"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>User Name</label>
                      <input
                        type="text"
                        class="form-control"
                        value="John Smith"
                        placeholder="Enter User Name"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Email</label>
                      <input
                        type="email"
                        class="form-control"
                        value="john@example.com"
                        placeholder="Enter Email Address"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Phone Number</label>
                      <input
                        type="text"
                        class="form-control"
                        value="+1 989-438-3131"
                        placeholder="Enter Phone Number"
                        name="name"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Role</label>
                      <input
                        type="text"
                        class="form-control"
                        value="Lorem ipsum"
                        placeholder="Enter Phone Number"
                        name="name"
                      />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="pass-group" id="passwordInput1">
                      <div class="form-group">
                        <label>Password</label>
                        <input
                          type="text"
                          class="form-control"
                          value="12345678"
                          placeholder=""
                        />
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="pass-group" id="passwordInput2">
                      <div class="form-group">
                        <label>Confirm Password</label>
                        <input
                          type="text"
                          class="form-control"
                          value="12345678"
                          placeholder=""
                        />
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Status</label>
                      <input
                        type="text"
                        class="form-control"
                        value="Active"
                        placeholder="Status"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div class="text-end">
                <button type="reset" class="btn btn-primary cancel me-2">Cancel</button>
                <b-button type="submit" variant="primary">Save Changes</b-button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      showPassword: false,
      showPassword2: false,
      password: null,
      password2: null,
      Role: ["Select Role", "Role 1", "Role 2"],
      Status: ["Select Status", "Active", "Inactive"],
    };
  },
  computed: {
    buttonLabel() {
      return this.showPassword ? "Hide" : "Show";
    },
    buttonLabel2() { // Rename the key to make it unique
      return this.showPassword2 ? "Hide" : "Show";
    },
  },
  methods: {
    toggleShow() {
      this.showPassword = !this.showPassword;
    },
    toggleShow2() {
      this.showPassword2 = !this.showPassword2;
    },
  },
};
</script>
