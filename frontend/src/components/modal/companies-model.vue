<template>
  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="#" class="sidebar-closes"><i class="fa-regular fa-circle-xmark"></i></a>
      </div>
      <div class="sidebar-body">
        <form action="#" autocomplete="off">
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
                  Company Name
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
                          class="form-control member-search-dropdown"
                          id="member_search1"
                          placeholder="Search Company"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont search-dropdown-item">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Hermann Groups
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Skiles LLC
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Kerluke Group
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>Schowalter Group
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Accentric Global
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Dexter Matrix
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Emporis Technologies
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>High Tech Lead
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Beacon Softwares
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>Global tech
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Customer -->

          <!-- By Plane -->
          <div class="accordion" id="accordionMain3">
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
                  Plans
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
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> All Plans
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Advanced
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Basic
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Enterprise
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Premium
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Free
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Plane -->

          <!-- By Plane -->
          <div class="accordion" id="accordionMain4">
            <div class="card-header-new" id="headingFour">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseFour"
                  aria-expanded="true"
                  aria-controls="collapseFour"
                >
                  Plans Type
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseFour"
              class="collapse"
              aria-labelledby="headingFour"
              data-bs-parent="#accordionExample4"
            >
              <div class="card-body-chat">
                <div id="checkBoxes2">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> All Plan Type
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Monthly
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Weekly
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Lifetime
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Plane -->

          <!-- Select Date -->
          <div class="accordion accordion-last" id="accordionMain2">
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
                      v-model="startdateOne"
                      class="form-control datetimepicker"
                      :editable="true"
                      :clearable="false"
                      placeholder="DD-MM-YYYY"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
                <div class="input-block mb-3">
                  <label class="form-control-label">To</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdateTwo"
                      class="form-control datetimepicker"
                      :editable="true"
                      :clearable="false"
                      placeholder="DD-MM-YYYY"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Select Date -->

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

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade modal-delete" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <div class="delete-modal-icon">
              <span><i class="feather feather-check-circle"></i></span>
            </div>
            <h3>Are You Sure?</h3>
            <p>You want delete company</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="modal-footer justify-content-center p-0">
              <button
                type="submit"
                data-bs-dismiss="modal"
                class="btn btn-primary paid-continue-btn me-2"
              >
                Yes, Delete
              </button>
              <button
                type="button"
                data-bs-dismiss="modal"
                class="btn btn-back cancel-btn"
              >
                No, Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->

  <!-- Add Companies Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="add_companies"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add New Company</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form action="companies.html">
          <div class="modal-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-field-item">
                  <h5 class="form-title">Company Profile</h5>
                  <div class="profile-picture">
                    <div class="upload-profile">
                      <div class="profile-img company-profile-img">
                        <img
                          id="company-img"
                          class="img-fluid me-0"
                          src="@/assets/img/companies/company-add-img.svg"
                          alt="profile-img"
                        />
                      </div>
                      <div class="add-profile">
                        <h5>Upload a New Photo</h5>
                        <span>Profile-pic.jpg</span>
                      </div>
                    </div>
                    <div class="img-upload">
                      <label class="btn btn-upload"> Upload <input type="file" /> </label>
                      <a class="btn btn-remove">Remove</a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-12">
                <div class="input-block mb-3">
                  <label class="form-label">Name </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Company Name"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Email Address </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Company Email"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Account Url </label>
                  <div class="url-text-box">
                    <input type="text" class="form-control" placeholder="Account URL" />
                    <span class="url-text">kanakku.com</span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="mb-2">Phone Number</label>
                  <vue-tel-input mode="international" class="form-control d-flex" id="phone" name="phone"
                          :defaultCountry="'US'"></vue-tel-input>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Website </label>
                  <input type="text" class="form-control" placeholder="Enter Website" />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-control-label">Password</label>
                  <div class="pass-group modal-password-field">
                    <input
                      type="password"
                      class="form-control pass-input"
                      placeholder="Password"
                    />
                    <span class="fas toggle-password fa-eye-slash"></span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-control-label">Confirm Password</label>
                  <div class="pass-group modal-password-field">
                    <input
                      type="password"
                      class="form-control pass-input-two"
                      placeholder="Confirm Password"
                    />
                    <span class="fas toggle-password-two fa-eye-slash"></span>
                  </div>
                </div>
              </div>
              <div class="col-md-12">
                <div class="input-block mb-3">
                  <label class="form-label">Company Address </label>
                  <textarea type="text" class="form-control" rows="3"></textarea>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Name</label>
                  <vue-select 
                    :options="Plan"
                    id="planname"
                    placeholder="Select Plan"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Type</label>
                  <vue-select 
                    :options="Type"
                    id="plantype"
                    placeholder="Select Plan Type"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Select Currency</label>
                  <vue-select 
                    :options="Currency"
                    id="currencyselect"
                    placeholder="Select Currency"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Select Language</label>
                  <vue-select 
                    :options="Language"
                    id="langselect"
                    placeholder="Select language"
                  />
                </div>
              </div>
              <div class="col-md-12">
                <div class="d-flex align-items-center mb-3">
                  <h6 class="mb-0">Status</h6>
                  <div class="status-toggle">
                    <input id="access-trail" class="check" type="checkbox" checked="" />
                    <label for="access-trail" class="checktoggle checkbox-bg"
                      >checkbox</label
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-back cancel-btn me-2"
            >
              Cancel
            </button>
            <button
              type="submit"
              data-bs-dismiss="modal"
              class="btn btn-primary paid-continue-btn"
            >
              Add New
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!-- /Add Companies Modal -->

  <!-- Edit Companies Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="edit_companies"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Company</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form action="companies.html">
          <div class="modal-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-field-item">
                  <h5 class="form-title">Company Profile</h5>
                  <div class="profile-picture">
                    <div class="upload-profile">
                      <div class="profile-img company-profile-img">
                        <img
                          id="edit-company-img"
                          class="img-fluid me-0"
                          src="@/assets/img/companies/company-01.svg"
                          alt="profile-img"
                        />
                      </div>
                      <div class="add-profile">
                        <h5>Upload a New Photo</h5>
                        <span>Profile-pic.jpg</span>
                      </div>
                    </div>
                    <div class="img-upload">
                      <label class="btn btn-upload"> Upload <input type="file" /> </label>
                      <a class="btn btn-remove">Remove</a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-12">
                <div class="input-block mb-3">
                  <label class="form-label">Name </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Company Name"
                    value="Hermann Groups"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Email Address </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Company Email"
                    value="info@example.com"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Account Url </label>
                  <div class="url-text-box">
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Account URL"
                      value="www.hru.example.com"
                    />
                    <span class="url-text">kanakku.com</span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="mb-2">Phone Number</label>
                  <vue-tel-input mode="international" class="form-control d-flex" id="phoneone" name="phone"
                          :defaultCountry="'US'"></vue-tel-input>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-label">Website </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Website"
                    value="www.example.com"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-control-label">Password</label>
                  <div class="pass-group modal-password-field">
                    <input
                      type="password"
                      class="form-control pass-input"
                      placeholder="Password"
                      value="12345"
                    />
                    <span class="fas toggle-password fa-eye-slash"></span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label class="form-control-label">Confirm Password</label>
                  <div class="pass-group modal-password-field">
                    <input
                      type="password"
                      class="form-control pass-input-two"
                      placeholder="Confirm Password"
                      value="12345"
                    />
                    <span class="fas toggle-password-two fa-eye-slash"></span>
                  </div>
                </div>
              </div>
              <div class="col-md-12">
                <div class="input-block mb-3">
                  <label class="form-label">Company Address </label>
                  <textarea type="text" class="form-control" rows="3">
22 Junior Avenue Duluth, GA 30097</textarea
                  >
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Name</label>
                  <vue-select 
                    :options="Free"
                    id="allplanfree"
                    placeholder="All Plans"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Type</label>
                  <vue-select 
                    :options="Lifetime"
                    id="lifetime"
                    placeholder="Monthly"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Select Currency</label>
                  <vue-select 
                    :options="Stated"
                    id="statedusd"
                    placeholder="United Stated Dollar (USD)"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="input-block mb-3">
                  <label>Select Language</label>
                  <vue-select 
                    :options="French"
                    id="langfrench"
                    placeholder="English"
                  />
                </div>
              </div>
              <div class="col-md-12">
                <div class="d-flex align-items-center mb-3">
                  <h6 class="mb-0">Status</h6>
                  <div class="status-toggle">
                    <input id="access-trail-2" class="check" type="checkbox" checked="" />
                    <label for="access-trail-2" class="checktoggle checkbox-bg"
                      >checkbox</label
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-back cancel-btn me-2"
            >
              Cancel
            </button>
            <button
              type="submit"
              data-bs-dismiss="modal"
              class="btn btn-primary paid-continue-btn"
            >
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!-- /Edit Companies Modal -->

  <!-- View Companies Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="view_companies"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Company Details</h4>
          </div>
          <div class="d-flex details-edit-link">
            <a
              href="#"
              class="modal-edit-link d-flex align-items-center"
              data-bs-toggle="modal"
              data-bs-target="#edit_companies"
              ><i class="feather feather-edit me-2"></i>Edit Company</a
            >
            <button
              type="button"
              class="btn-close ms-2"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
        </div>
        <div class="modal-body pb-0">
          <div class="row">
            <div class="col-md-12">
              <div class="form-field-item">
                <div class="profile-picture company-detail-head">
                  <div class="upload-profile">
                    <div class="profile-img company-profile-img">
                      <img
                        id="view-company-img"
                        class="img-fluid me-0"
                        src="@/assets/img/companies/company-01.svg"
                        alt="profile-img"
                      />
                    </div>
                    <div class="add-profile">
                      <h5>Hermann Groups</h5>
                      <span>Hermllrich@example.com</span>
                    </div>
                  </div>
                  <span class="badge bg-success-light d-inline-flex align-items-center"
                    ><i class="feather feather-check me-1"></i>Active</span
                  >
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <div class="plane-basic-info">
                <h5>Basic Info</h5>
                <div class="row">
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Account URL</h6>
                      <p>hru.example.com</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Phone Number</h6>
                      <p>+1 15541 54544</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Website</h6>
                      <p>www.example.com</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Company Address</h6>
                      <p>22 Junior Avenue <br />Duluth, GA 30097</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Currency</h6>
                      <p>United Stated Dollar (USD)</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Language</h6>
                      <p>English</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <div class="plane-basic-info plane-detail">
                <h5>Plan Details</h5>
                <div class="row">
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Plan Name</h6>
                      <p>Enterprise</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Plan Type</h6>
                      <p>Yearly</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Price</h6>
                      <p>$200</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Register Date</h6>
                      <p>15 Jan 2024</p>
                    </div>
                  </div>
                  <div class="col-md-4 col-sm-6">
                    <div class="basic-info-detail">
                      <h6>Expiring On</h6>
                      <p>15 Jan 2025</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /View Companies Modal -->

  <!-- Change Plane Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="change_pane"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Update Package</h4>
          </div>
          <button
            type="button"
            class="btn-close ms-2"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form action="#">
          <div class="modal-body">
            <div class="row">
              <div class="col-md-12">
                <div class="plane-basic-info plane-detail">
                  <h5>Current Plan Details</h5>
                  <div class="row">
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Company Name</h6>
                        <p>Hermann Groups</p>
                      </div>
                    </div>
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Plan Name</h6>
                        <p>Enterprise</p>
                      </div>
                    </div>
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Plan Type</h6>
                        <p>Yearly</p>
                      </div>
                    </div>
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Price</h6>
                        <p>$200</p>
                      </div>
                    </div>
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Register Date</h6>
                        <p>15 Jan 2024</p>
                      </div>
                    </div>
                    <div class="col-md-4 col-sm-6">
                      <div class="basic-info-detail">
                        <h6>Expiring On</h6>
                        <p>15 Jan 2025</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-12">
                <div class="plane-basic-info plane-detail">
                  <h5>Change Company Plan</h5>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label>Plan Name</label>
                        <vue-select 
                          :options="Enterprise"
                          id="enterpriseplan"
                          placeholder="Enterprise"
                        />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label>Plan Type</label>
                        <vue-select 
                          :options="Lifetime"
                          id="yearlyone"
                          placeholder="Yearly"
                        />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label class="form-label">Amount </label>
                        <input type="text" class="form-control" />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label class="form-control-label">Payment Date</label>
                        <div class="cal-icon">
                          <date-picker
                            v-model="startdate"
                            class="form-control datetimepicker"
                            :editable="true"
                            :clearable="false"
                            placeholder="DD-MM-YYYY"
                            :input-format="dateFormat"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label class="form-control-label">Next Payment Date</label>
                        <div class="cal-icon">
                          <date-picker
                            v-model="startdateThree"
                            class="form-control datetimepicker"
                            :editable="true"
                            :clearable="false"
                            placeholder="DD-MM-YYYY"
                            :input-format="dateFormat"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-block mb-3">
                        <label class="form-control-label">Expiring On</label>
                        <div class="cal-icon">
                          <date-picker
                            v-model="startdateFour"
                            class="form-control datetimepicker"
                            :editable="true"
                            :clearable="false"
                            placeholder="DD-MM-YYYY"
                            :input-format="dateFormat"
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
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-back cancel-btn me-2"
            >
              Cancel
            </button>
            <button
              type="submit"
              data-bs-dismiss="modal"
              class="btn btn-primary paid-continue-btn"
            >
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!-- /Change Plane Modal -->
</template>

<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
const currentDateTwo = ref(new Date());
const currentDateThree = ref(new Date());
const currentDateFour = ref(new Date());
export default {
  data() {
    return {
      Plan: ["Select Plan", "All Plans", "Advanced", "Basic", "Enterprise", "Premium", "Free"],
      Type: ["Select Plan Type", "Monthly", "Yearly", "Lifetime"],
      Currency: ["Select Currency", "₹", "$", "£", "€"],
      Language: ["Select language", "English", "French", "Spanish", "German"],
      Free: ["All Plans", "Advanced", "Basic", "Enterprise", "Premium", "Free"],
      Lifetime: ["Monthly", "Yearly", "Lifetime"],
      Stated: ["United Stated Dollar (USD)", "$", "£", "€"],
      French: ["English", "French", "Spanish", "German"],
      Enterprise: ["Enterprise", "Advanced", "Basic", "Premium", "Free"],
      startdate: currentDate,
      startdateOne: currentDateOne,
      startdateTwo: currentDateTwo,
      startdateThree: currentDateThree,
      startdateFour: currentDateFour,
      dateFormat: "dd-MM-yyyy",
    }
  },
};
</script>
