<template>
  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="javascript:;" class="sidebar-closes"><i class="fa-regular fa-circle-xmark"></i></a>
      </div>
      <div class="sidebar-body">
        <form action="javascript:;" autocomplete="off">
          <!-- Customer -->
          <div class="accordion" id="accordionMain1">
            <div class="card-header-new" id="headingOne">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  Customer
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseOne"
              class="collapse show"
              aria-labelledby="headingOne"
              data-bs-parent="#accordionExample1"
            >
              <div class="card-body-chat">
                <div class="row">
                  <div class="col-md-12">
                    <div id="checkBoxes1">
                      <div class="form-custom">
                        <input
                          type="text"
                          class="form-control"
                          id="member_search1"
                          placeholder="Search here"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> John Smith
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Johnny
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Robert
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Sharonda
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Pricilla
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Randall
                            </label>
                          </div>
                          <div class="view-all">
                            <a href="javascript:void(0);" class="viewall-button-One"
                              ><span class="me-2">View All</span
                              ><span><i class="fa fa-circle-chevron-down"></i></span
                            ></a>
                          </div>
                        </div>
                        <!-- /View All -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Customer -->

          <!-- Select Date -->
          <div class="accordion" id="accordionMain2">
            <div class="card-header-new" id="headingTwo">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseTwo"
                  aria-expanded="true"
                  aria-controls="collapseTwo"
                >
                  Select Date
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseTwo"
              class="collapse"
              aria-labelledby="headingTwo"
              data-bs-parent="#accordionExample2"
            >
              <div class="card-body-chat">
                <div class="input-block mb-3">
                  <label class="form-control-label">From</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdate"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
                <div class="input-block mb-3">
                  <label class="form-control-label">To</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdate1"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Select Date -->

          <!-- By Status -->
          <div class="accordion accordion-last" id="accordionMain3">
            <div class="card-header-new" id="headingThree">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseThree"
                  aria-expanded="true"
                  aria-controls="collapseThree"
                >
                  By Status
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseThree"
              class="collapse"
              aria-labelledby="headingThree"
              data-bs-parent="#accordionExample3"
            >
              <div class="card-body-chat">
                <div id="checkBoxes2">
                  <div class="form-custom">
                    <input
                      type="text"
                      class="form-control"
                      id="member_search2"
                      placeholder="Search here"
                    />
                    <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                  </div>
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Active
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Restricted
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Status -->
          <div class="filter-buttons">
            <button
              type="submit"
              class="d-inline-flex align-items-center justify-content-center btn w-100 btn-primary"
            >
              Apply
            </button>
            <button
              type="submit"
              class="d-inline-flex align-items-center justify-content-center btn w-100 btn-secondary"
            >
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!--/Add Asset -->

  <!-- Add User -->
  <div class="modal custom-modal modal-lg fade" id="add_user" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add User</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">
              <div class="card-body">
                <div class="form-groups-item">
                  <h5 class="form-title">Profile Picture</h5>
                  <div class="profile-picture">
                    <div class="upload-profile">
                      <div class="profile-img">
                        <img
                          id="blah"
                          class="avatar"
                          src="@/assets/img/profiles/avatar-10.jpg"
                          alt="profile-img"
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
                      <div class="input-block mb-3">
                        <label>First Name</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter First Name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Last Name</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Last Name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>User Name</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter User Name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Email</label>
                        <input
                          type="email"
                          class="form-control"
                          placeholder="Enter Email Address"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Phone Number</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Phone Number"
                          name="name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Role</label>

                        <vue-select
                          :options="Userrole"
                          id="userrole"
                          placeholder="Select Role"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="pass-group" id="3">
                        <div class="input-block">
                          <label>Password</label>
                          <input
                            type="password"
                            class="form-control pass-input"
                            placeholder=""
                          />
                          <span class="toggle-password feather-eye"></span>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="pass-group" id="passwordInput2">
                        <div class="input-block">
                          <label>Confirm Password</label>
                          <input
                            type="password"
                            class="form-control pass-input"
                            placeholder=""
                          />
                          <span class="toggle-password feather-eye"></span>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block">
                        <label>Status</label>

                        <vue-select
                          :options="UserStatus"
                          id="userstatus"
                          placeholder="Select Status"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add User</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add User -->

  <!-- Add User -->
  <div class="modal custom-modal modal-lg fade" id="edit_user" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit User</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">
              <div class="card-body">
                <div class="form-groups-item">
                  <h5 class="form-title">Profile Picture</h5>
                  <div class="profile-picture">
                    <div class="upload-profile">
                      <div class="profile-img">
                        <img
                          id="blah2"
                          class="avatar"
                          src="@/assets/img/profiles/avatar-10.jpg"
                          alt="profile-img"
                        />
                      </div>
                      <div class="add-profile">
                        <h5>Upload a New Photo</h5>
                        <span>Profile-pic.jpg</span>
                      </div>
                    </div>
                    <div class="img-upload">
                      <label class="btn btn-primary">
                        Upload <input type="file" />
                      </label>
                      <a class="btn btn-remove">Remove</a>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>First Name</label>
                        <input
                          type="text"
                          value="John"
                          class="form-control"
                          placeholder="Enter First Name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
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
                      <div class="input-block mb-3">
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
                      <div class="input-block mb-3">
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
                      <div class="input-block mb-3">
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
                      <div class="input-block mb-3">
                        <label>Role</label>

                        <vue-select
                          :options="Userroleone"
                          id="userroleone"
                          placeholder="Role 1"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="pass-group" id="passwordInput1">
                        <div class="input-block">
                          <label>Password</label>
                          <input
                            type="password"
                            class="form-control pass-input"
                            value="12345678"
                            placeholder=""
                          />
                          <span class="toggle-password feather-eye"></span>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="pass-group" id="passwordInput4">
                        <div class="input-block">
                          <label>Confirm Password</label>
                          <input
                            type="password"
                            class="form-control pass-input"
                            value="12345678"
                            placeholder=""
                          />
                          <span class="toggle-password feather-eye"></span>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block">
                        <label>Status</label>

                        <vue-select
                          :options="UserStatusone"
                          id="userstatusone"
                          placeholder="Active"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit User -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Users</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <a href="javascript:;" class="btn btn-primary paid-continue-btn">Delete</a>
              </div>
              <div class="col-6">
                <a
                  href="javascript:;"
                  data-bs-dismiss="modal"
                  class="btn btn-primary paid-cancel-btn"
                  >Cancel</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDate1 = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      startdate1: currentDate1,
      dateFormat: "dd-MM-yyyy",
      Userrole: ["Select Role", "Role 1", "Role 2"],
      UserStatus: ["Select Status", "Active", "Inactive"],
      Userroleone: ["Select Role", "Role 1", "Role 2"],
      UserStatusone: ["Select Status", "Active", "Inactive"],
    };
  },
  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      const popupToggleElements = document.getElementsByClassName("popup-toggle");
      const toggleSidebarElement = document.querySelector(".toggle-sidebar");
      const bodyElement = document.body;

      if (popupToggleElements.length > 0) {
        for (let i = 0; i < popupToggleElements.length; i++) {
          popupToggleElements[i].addEventListener("click", function () {
            toggleSidebarElement.classList.add("open-filter");
            bodyElement.classList.add("filter-opened");
          });
        }

        const sidebarCloseElements = document.getElementsByClassName("sidebar-closes");
        for (let i = 0; i < sidebarCloseElements.length; i++) {
          sidebarCloseElements[i].addEventListener("click", function () {
            toggleSidebarElement.classList.remove("open-filter");
            bodyElement.classList.remove("filter-opened");
          });
        }
      }
    });
    document.addEventListener("DOMContentLoaded", function () {
      function initializeViewAll(classPrefix) {
        var viewallOnes = document.getElementsByClassName("viewall-" + classPrefix);
        var viewallButton = document.getElementsByClassName(
          "viewall-button-" + classPrefix
        )[0];

        if (viewallOnes.length > 0 && viewallButton) {
          for (var i = 0; i < viewallOnes.length; i++) {
            viewallOnes[i].style.display = "none";
          }

          viewallButton.addEventListener("click", function () {
            var buttonText = viewallButton.textContent;
            for (var i = 0; i < viewallOnes.length; i++) {
              viewallOnes[i].style.display =
                viewallOnes[i].style.display === "none" ? "block" : "none";
            }

            viewallButton.textContent =
              buttonText === "Close All" ? "View All" : "Close All";
          });
        }
      }

      if (document.getElementsByClassName("viewall-One").length > 0) {
        initializeViewAll("One");
      }

      if (document.getElementsByClassName("viewall-Two").length > 0) {
        initializeViewAll("Two");
      }
    });
  },
};
</script>
