<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header">
                <h5 class="setting-menu">Account Settings</h5>
              </div>
              <div class="row">
                <div class="profile-picture">
                  <div class="upload-profile me-2">
                    <div class="profile-img">
                      <img id="blah" class="avatar" src="@/assets/img/profiles/avatar-10.jpg" alt="profile-img" />
                    </div>
                  </div>
                  <div class="img-upload">
                    <label class="btn btn-primary">
                      Upload new picture <input type="file" />
                    </label>
                    <a class="btn btn-remove">Delete</a>
                    <p class="mt-1">
                      Logo Should be minimum 152 * 152 Supported File format JPG,PNG,SVG
                    </p>
                  </div>
                </div>

                <div class="col-lg-12">
                  <div class="form-title">
                    <h5>General Information</h5>
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>First Name</label>
                    <input type="text" class="form-control" placeholder="Enter First Name" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Last Name</label>
                    <input type="text" class="form-control" placeholder="Enter Last Name" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Email</label>
                    <input type="text" class="form-control" placeholder="Enter Email Address" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Mobile Number</label>
                    <input type="text" class="form-control" placeholder="Enter Mobile Number" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-0">
                    <label>Gender</label>
                    <vue-select :options="Gender" id="gender" placeholder="Select Gender" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Date of Birth</label>
                    <div class="cal-icon">
                      <date-picker v-model="startdate" class="datetimepicker form-control" :editable="true"
                        :clearable="false" :input-format="dateFormat" />
                    </div>
                  </div>
                </div>
                <div class="col-lg-12">
                  <div class="form-title">
                    <h5>Address Information</h5>
                  </div>
                </div>
                <div class="col-lg-12">
                  <div class="input-block mb-3">
                    <label>Address</label>
                    <input type="text" class="form-control" placeholder="Enter your Address" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Country</label>
                    <input type="text" class="form-control" placeholder="Enter your Country" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>State</label>
                    <input type="text" class="form-control" placeholder="Enter your State" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>City</label>
                    <input type="text" class="form-control" placeholder="Enter your City" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Postal Code</label>
                    <input type="text" class="form-control" placeholder="Enter Your Postal Code" />
                  </div>
                </div>
                <div class="col-lg-12">
                  <div class="btn-path text-end">
                    <a href="javascript:void(0);" class="btn btn-cancel bg-primary-light me-3">Cancel</a>
                    <a href="javascript:void(0);" class="btn btn-primary">Save Changes</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
export default {
  setup() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
      Gender: ["Select Gender", "Male", "Female"],
    };
  },
};
</script>
