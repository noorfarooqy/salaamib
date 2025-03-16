<template>
  <!-- Add Vendor Modal -->
  <div class="modal custom-modal fade" id="add_countries" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Countries</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Code</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Country Code"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country ID</label>
                <input type="text" class="form-control" placeholder="Enter Country ID" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>Country Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Country Name"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Countries</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Vendor Modal -->
  <div class="modal custom-modal fade" id="edit_countries" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Countries</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Code</label>
                <input
                  type="text"
                  class="form-control"
                  value="684"
                  placeholder="Enter Country Code"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country ID</label>
                <input
                  type="text"
                  class="form-control"
                  value="AS"
                  placeholder="Select Date"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>Country Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="American Samoa"
                  placeholder="Enter Reference Number"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->

  <!-- Add Vendor Modal -->
  <div class="modal custom-modal fade" id="add_state" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add State</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Code</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Country Code"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Country Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>State Name</label>
                <input type="text" class="form-control" placeholder="Enter State Name" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add State</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Vendor Modal -->
  <div class="modal custom-modal fade" id="edit_state" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit State</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Code</label>
                <input
                  type="text"
                  class="form-control"
                  value="As"
                  placeholder="Enter Country Code"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="American Samoa"
                  placeholder="Enter Country Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>State Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="Swains Island"
                  placeholder="Enter State Name"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->
  <!-- Add Vendor Modal -->
  <div class="modal custom-modal fade" id="add_cities" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add City</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Name</label>
                <vue-select :options="Countrymodal" placeholder="Select Country Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>State Name</label>
                <vue-select :options="State" id="state" placeholder="Select State Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>City Name</label>
                <input type="text" class="form-control" placeholder="Enter City Name" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Cities</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Vendor Modal -->
  <div class="modal custom-modal fade" id="edit_cities" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit City</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Country Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="American Samoa"
                  placeholder="Enter Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>State Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="Swains Island"
                  placeholder="Select Date"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>City Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="Gandzasar"
                  placeholder="Enter Reference Number"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->
  <!-- Add FAQ Modal -->
  <div class="modal custom-modal fade" id="add_faq" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add FAQ</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12">
              <div class="form-group">
                <label>Title Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Title" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mt-3">
                <label>Category <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Category" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mt-3">
                <label>Details <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Details" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-0 mt-3">
                <div class="check-mark-status d-flex justify-content-between">
                  <h6 class="label-text">Status</h6>
                  <div class="status-toggle">
                    <input id="rating_1" class="check" type="checkbox" checked="" />
                    <label for="rating_1" class="checktoggle checkbox-bg">checkbox</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add FAQ</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add FAQ Modal -->

  <!-- Edit FAQ Modal -->
  <div class="modal custom-modal fade" id="edit_faq" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit FAQ</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Title Name</label>
                <input
                  type="text"
                  class="form-control"
                  value=""
                  placeholder="Enter Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mt-3">
                <label>Category</label>
                <input type="text" class="form-control" value="" placeholder="Category" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mt-3">
                <label>Details</label>
                <input type="text" class="form-control" value="" placeholder="Details" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="input-block mb-0">
                <div class="check-mark-status d-flex justify-content-between">
                  <h6 class="label-text mt-3">Status</h6>
                  <div class="status-toggle mt-3">
                    <input id="rating_2" class="check" type="checkbox" checked="" />
                    <label for="rating_2" class="checktoggle checkbox-bg">checkbox</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit FAQ Modal -->
  <!-- Add Expenses Modal -->
  <div class="modal custom-modal modal-lg fade" id="add_expenses" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Expenses</h4>
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
                <div class="border-0 pb-0">
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense ID</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Expense ID"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Reference No"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Amount </label>
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Enter Amount"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Mode</label>
                        <vue-select
                          :options="Mode"
                          id="mode"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Expense Date </label>
                        <date-picker
                          v-model="startdate"
                          type="text"
                          class="datetimepicker form-control"
                          :editable="true"
                          :clearable="false"
                          :input-format="dateFormat"
                          placeholder="Select Expense Date"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Status</label>
                        <vue-select
                          :options="Status"
                          id="statusone"
                          placeholder="Select Payment Status"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12 description-box">
                      <div class="input-block mb-3" id="summernote_container">
                        <label class="form-control-label">Description</label>
                        <editor v-model="content" />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12">
                      <div class="input-block">
                        <label>Attachment</label>
                        <div class="input-block service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign" />
                          <div id="frames"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Expenses</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Expenses Modal -->
  <!-- Edit Expenses Modal -->
  <div class="modal custom-modal modal-lg fade" id="edit_expenses" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Expenses</h4>
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
                <div class="border-0 pb-0">
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense ID</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Expense ID"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Reference No"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Amount </label>
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Enter Amount"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Mode</label>
                        <vue-select
                          :options="Mode"
                          id="mode1"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense Date </label>
                        <date-picker
                          v-model="startdateOne"
                          type="text"
                          class="datetimepicker form-control"
                          :editable="true"
                          :clearable="false"
                          :input-format="dateFormat"
                          placeholder="Select Expense Date"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Status</label>
                        <vue-select
                          :options="Status"
                          id="payment"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12 description-box">
                      <div class="input-block mb-3" id="summernote_container2">
                        <label class="form-control-label">Description</label>
                        <editor v-model="content" />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12">
                      <div class="input-block">
                        <label>Attachment</label>
                        <div class="input-block service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign2" />
                          <div id="frames2"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Expenses Modal -->
  <!-- Add Vendor Modal -->
  <div class="modal custom-modal fade" id="add_vendor" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Vendor</h4>
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
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" placeholder="Enter Name" />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Email</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Email Address"
                />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Phone Number</label>
                <input
                  type="number"
                  class="form-control"
                  placeholder="Enter Phone Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-0">
                <label>Closing Balance</label>
                <input
                  type="number"
                  class="form-control"
                  placeholder="Enter Closing Balance Amount"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="#" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add Vendor</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Vendor Modal -->
  <div class="modal custom-modal fade" id="edit_vendor" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Vendor</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="John Smith"
                  placeholder="Enter Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Email</label>
                <input
                  type="text"
                  class="form-control"
                  value="john@example.com"
                  placeholder="Select Date"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Phone Number</label>
                <input
                  type="text"
                  class="form-control"
                  value="+1 989-438-3131"
                  placeholder="Enter Reference Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Balance</label>
                <input
                  type="text"
                  class="form-control"
                  value="$4200"
                  placeholder="Enter Reference Number"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->

  <!-- Add Category Modal -->
  <div class="modal custom-modal fade" id="add_category" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Category</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">
              <div class="card-body">
                <div class="form-group-item border-0 pb-0 mb-0">
                  <div class="row">
                    <div class="col-lg-12 col-sm-12">
                      <div class="form-group">
                        <label>Name <span class="text-danger">*</span></label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Title"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Slug</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Slug"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Parent Category</label>
                        <vue-select
                          :options="Parent_Category"
                          id="parents"
                          placeholder="None"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="form-group mb-0 pb-0">
                        <label>Image</label>
                        <div class="form-group service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign" />
                          <div id="frames"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Category</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Category Modal -->

  <!-- Add Category Modal -->
  <div class="modal custom-modal fade" id="edit_category" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Category</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">
              <div class="card-body">
                <div class="form-group-item border-0 pb-0 mb-0">
                  <div class="row">
                    <div class="col-lg-12 col-sm-12">
                      <div class="form-group">
                        <label>Name <span class="text-danger">*</span></label>
                        <input
                          type="text"
                          class="form-control"
                          value="Advertising"
                          placeholder="Enter Title"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Slug</label>
                        <input
                          type="text"
                          class="form-control"
                          value="advertising"
                          placeholder="Enter Slug"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="input-block mb-3">
                        <label>Parent Category</label>
                        <vue-select
                          :options="Parent_Category1"
                          id="parent2"
                          placeholder="None"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-sm-12 mt-3">
                      <div class="form-group mb-0 pb-0">
                        <label>Image</label>
                        <div class="form-group service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign" />
                          <div id="frames"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->
  <!-- Add Units Modal -->
  <div class="modal custom-modal fade" id="add_unit" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Units</h4>
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
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Name" />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Symbol <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Symbol" />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-0">
                <label>Parent Unit <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Parent Unit" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:void(0);"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:void(0);"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Unit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Units Modal -->

  <!-- Add Units Modal -->
  <div class="modal custom-modal fade" id="edit_unit" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Units</h4>
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
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Name </label>
                <input
                  type="text"
                  class="form-control"
                  value="Kilogram"
                  placeholder="Enter Title"
                />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Symbol</label>
                <input
                  type="text"
                  class="form-control"
                  value="Slug"
                  placeholder="Enter Slug"
                />
              </div>
            </div>
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-0">
                <label>Parent Unit</label>
                <input
                  type="text"
                  class="form-control"
                  value="kg"
                  placeholder="Parent Unit"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:void(0);"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:void(0);"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Units Modal -->
  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>{{ Delete }}</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <button
                  type="reset"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-continue-btn"
                >
                  Delete
                </button>
              </div>
              <div class="col-6">
                <button
                  type="submit"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-cancel-btn"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
  <!-- Delete Paid Modal -->
  <div class="modal custom-modal fade" id="delete_paid" role="dialog">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>{{ Delete }}</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <a href="javascript:void(0);" class="btn btn-primary paid-continue-btn"
                  >Delete</a
                >
              </div>
              <div class="col-6">
                <a
                  href="javascript:void(0);"
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
  <!-- /Delete Paid Modal -->
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
                          :options="Role"
                          id="role"
                          placeholder="Select Status"
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
                          :options="Status1"
                          id="status2"
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
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
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
                          :options="Role"
                          id="role2"
                          placeholder="Select Status"
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
                          :options="Status1"
                          id="status3"
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
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit User -->
  <!-- Add Role Modal -->
  <div class="modal custom-modal fade" id="add_role" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Role</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Role Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Role Name" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Close</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Role Modal -->

  <!-- Edit Role Modal -->
  <div class="modal custom-modal fade" id="edit_role" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Role</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Role Name <span class="text-danger">*</span></label>
                <input
                  type="text"
                  class="form-control"
                  Value="Admin"
                  placeholder="Enter Role Name"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Close</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Role Modal -->
  <!-- Add Page -->
  <div class="modal custom-modal modal-lg fade" id="add_page" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">{{ title }}</h4>
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
                <div class="form-groups-item border-0 pb-0">
                  <div class="row">
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Title</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Title"
                        />
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label
                          >Slug
                          <span class="optional">
                            (If you leave it empty, it will be generated
                            automatically.)</span
                          ></label
                        >
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Slug"
                        />
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label
                          >Description <span class="optional"> (Meta Tag)</span></label
                        >
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Description"
                        />
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Keywords <span class="optional"> (Meta Tag)</span></label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Keywords"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Language</label>
                        <vue-select
                          :options="Language"
                          id="language"
                          placeholder="Select Language"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-12">
                      <div class="input-block mb-3">
                        <label>Location</label>
                        <div>
                          <label class="custom_radio me-3">
                            <input type="radio" name="payment" checked />
                            <span class="checkmark"></span> Top Menu
                          </label>
                          <label class="custom_radio">
                            <input type="radio" name="payment" />
                            <span class="checkmark"></span> Quick Links
                          </label>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-12">
                      <div class="input-block mb-3">
                        <label>Visibility</label>
                        <div>
                          <label class="custom_radio me-3">
                            <input type="radio" name="payment" checked />
                            <span class="checkmark"></span> Show
                          </label>
                          <label class="custom_radio">
                            <input type="radio" name="payment" />
                            <span class="checkmark"></span> Hide
                          </label>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-12">
                      <div class="input-block" id="summernote_container">
                        <label class="form-control-label">Description</label>
                        <editor v-model="content" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Page</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Page -->
  <!-- Modal -->
  <div class="modal custom-modal fade" id="pages_edit" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Page</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Page Title(English)</label>
                <input type="text" class="form-control" placeholder="About Us" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Page Slug</label>
                <input type="text" class="form-control" placeholder="about-us" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Page Content(English)</label>
                <textarea
                  rows="5"
                  cols="5"
                  class="form-control"
                  placeholder="about us page contents"
                ></textarea>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:void(0);" data-bs-dismiss="modal" class="btn btn-back me-2"
            >Back</a
          >
          <a href="javascript:void(0);" data-bs-dismiss="modal" class="btn btn-primary"
            >Save</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="page_delete" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Pages list</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <a href="javascript:;" class="btn btn-primary paid-continue-btn"
                  >Delete</a
                >
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
  <!-- Add Tax & Discount Modal -->
  <div class="modal custom-modal fade" id="add_discount" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Tax & Discount</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Rate</label>
                <input type="number" class="form-control" placeholder="120" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Discount Amount</label>
                <input type="number" class="form-control" placeholder="0" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Tax</label>
                <vue-select :options="Tax" placeholder="N/A" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer add-tax-btns">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn add-btn-cancel-btn"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary add-tax-save-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Tax & Discount Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_discount" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 justify-content-center pb-0">
          <div class="form-header modal-header-title text-center mb-0">
            <h4 class="mb-2">{{ Delete }}</h4>
            <p>Are you sure want to delete?</p>
          </div>
        </div>
        <div class="modal-body">
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <a
                  href="javascript:;"
                  data-bs-dismiss="modal"
                  class="btn btn-primary paid-continue-btn"
                  >Delete</a
                >
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

  <!-- Edit Bank Details Modal -->
  <div class="modal custom-modal fade" id="bank_details" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Bank Details</h4>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Bank Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Bank Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Account Number <span class="text-danger">*</span></label>
                <input
                  type="number"
                  class="form-control"
                  placeholder="Enter Account Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Branch Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Branch Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>IFSC Code <span class="text-danger">*</span></label>
                <input type="number" class="form-control" placeholder="Enter IFSC COde" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Back</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Bank Details Modal -->
  <!-- Pay Now Modal -->
  <div class="modal custom-modal fade pay-modal" id="paynow_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="modal-title">Invoice <span>#INV 00001</span></h4>
            <h5><span>Due Date : </span> 03 Jun 2023</h5>
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
            <div class="payment-heading">
              <h5>Select a Payment Method</h5>
            </div>
            <div class="input-block mb-3 paynow-tab">
              <ul class="nav nav-pills d-flex row" id="pills-tab" role="tablist">
                <li class="nav-item col-sm-4" role="presentation">
                  <button
                    class="nav-link active cash"
                    id="pills-home-tab"
                    data-bs-toggle="pill"
                    data-bs-target="#pills-home"
                    type="button"
                    role="tab"
                    aria-controls="pills-home"
                    aria-selected="true"
                  >
                    Cash<i class="feather feather-dollar-sign"></i>
                  </button>
                </li>
                <li class="nav-item col-sm-4" role="presentation">
                  <button
                    class="nav-link cheque"
                    id="pills-profile-tab"
                    data-bs-toggle="pill"
                    data-bs-target="#pills-profile"
                    type="button"
                    role="tab"
                    aria-controls="pills-profile"
                    aria-selected="false"
                  >
                    Cheque<i class="feather feather-file-text"></i>
                  </button>
                </li>
                <li class="nav-item col-sm-4" role="presentation">
                  <button
                    class="nav-link cheque"
                    data-bs-toggle="pill"
                    data-bs-target="#pills-profile"
                    type="button"
                    role="tab"
                    aria-controls="pills-profile"
                    aria-selected="false"
                  >
                    CreditCard<i class="feather feather-file-text"></i>
                  </button>
                </li>
              </ul>
            </div>
            <div class="tab-content pt-0" id="pills-tabContent">
              <div
                class="tab-pane fade show active"
                id="pills-home"
                role="tabpanel"
                aria-labelledby="pills-home-tab"
              >
                <div class="input-block mb-3">
                  <label>Amount <span class="text-danger"> *</span></label>
                  <input type="text" class="form-control" placeholder="Enter Amount" />
                </div>
              </div>
              <div
                class="tab-pane fade"
                id="pills-profile"
                role="tabpanel"
                aria-labelledby="pills-profile-tab"
              >
                <div class="input-block mb-3">
                  <label>Amount <span class="text-danger"> *</span></label>
                  <input type="text" class="form-control" placeholder="Enter Amount" />
                </div>
                <div class="input-block mb-3">
                  <label>Cheque Number <span class="text-danger"> *</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Cheque Number"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >pay Now</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Pay Now Modal -->
  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Customer</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <button
                  type="reset"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-continue-btn"
                >
                  Delete
                </button>
              </div>
              <div class="col-6">
                <button
                  type="submit"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-cancel-btn"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
  <!-- View Modal -->
  <div class="modal custom-modal fade" id="view_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content view-delivery-challans">
        <div
          class="modal-header border-0 pb-0 justify-content-end d-flex align-items-center"
        >
          <div class="file-link mb-0">
            <button class="download_btn download-link">
              <i class="fa fa-cloud-download me-1" aria-hidden="true"></i>
              <span>Download</span>
            </button>
            <a href="javascript:window.print()" class="print-link">
              <i class="fa fa-print me-1" aria-hidden="true"></i>
              <span >Print</span>
            </a>
          </div>
        </div>
        <div class="modal-body invoice-one">
          <div class="invoice-wrapper download_section">
            <div class="inv-content">
              <div class="invoice-header p-0">
                <div class="inv-header-left">
                  <h4>DELIVERY CHALLAN</h4>
                  <h5>Dreams Technologies Pvt Ltd</h5>
                  <h6>Mobile 8072687299</h6>
                </div>
                <div class="inv-header-right">
                  <h3 class="mb-3">Delivery Challan</h3>
                  <h6 class="mb-1">Invoice # : <span> INV-1</span></h6>
                  <h6 class="mb-1">Invoice Date :<span> 07-10-2023</span></h6>
                  <p>Due Date : <span>07-12-2023</span></p>
                </div>
              </div>
              <span class="line my-4"></span>
              <div class="patient-infos">
                <div class="row">
                  <div class="col-sm-4">
                    <div class="patient-detailed">
                      <div class="bill-add">Customer Details :</div>
                      <div class="customer-name">
                        <h4 class="mb-1">Test Customer</h4>
                        <h4 class="mb-1">Test Company</h4>
                        <p><span>GSTIN : ACWR000054321</span></p>
                        <p><span>Phone Number : +91 1234567890</span></p>
                        <p><span>Email : delive@example.com</span></p>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="patient-detailed">
                      <div class="bill-add">Billing Address :</div>
                      <div class="add-details">
                        Walter Roberson <br />
                        299 Star Trek Drive, Panama City,<br />
                        Florida, 32405,<br />
                        USA
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="patient-detailed">
                      <div class="bill-add">Shipping Address :</div>
                      <div class="add-details">
                        Walter Roberson <br />
                        299 Star Trek Drive, Panama City,<br />
                        Florida, 32405,<br />
                        USA
                      </div>
                    </div>
                  </div>
                </div>
                <div class="reference">
                  <h4>Reference</h4>
                  <p>
                    Keep the Delivery Challan for reference in the future. Now it's simple
                    to create an invoice, download it
                  </p>
                  <hr />
                </div>
              </div>
              <div class="invoice-table">
                <div class="table-responsive">
                  <table>
                    <thead>
                      <tr class="ecommercetable">
                        <th class="table_width_1">#</th>
                        <th>Item</th>
                        <th class="text-end">Quantity</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1</td>
                        <td class="text-start">Accounting Software Maintainence</td>
                        <td class="text-end">3</td>
                      </tr>
                      <tr>
                        <td>2</td>
                        <td class="text-start">Man Power Support</td>
                        <td class="text-end">1</td>
                      </tr>
                      <tr>
                        <td>3</td>
                        <td class="text-start">Transportation Fee</td>
                        <td class="text-end">2</td>
                      </tr>
                      <tr>
                        <td>4</td>
                        <td class="text-start">Spars Replacement Charges</td>
                        <td class="text-end">5</td>
                      </tr>
                      <tr>
                        <td>5</td>
                        <td class="text-start">Materials Handling</td>
                        <td class="text-end">1</td>
                      </tr>
                    </tbody>
                  </table>
                  <h5 class="text-end">Total Quantity : 12</h5>
                </div>
              </div>

              <div class="authorization text-end">
                <h6>For YOUR BUSINESS NAME</h6>
                <img src="@/assets/img/signature.png" class="my-3" alt="signature-img" />
                <h6>Authorized Signatory</h6>
              </div>

              <div class="row">
                <div class="col-12">
                  <div class="terms-condition p-0">
                    <span>Terms & Conditions:</span>
                    <ol>
                      <li>
                        This is a GST based invoice bill, Which is applicable for TDS
                        Deduction
                      </li>
                      <li>
                        We are not the manufactures, company will stand for warranty as
                        per their terms and conditions.
                      </li>
                    </ol>
                  </div>
                </div>
              </div>
            </div>
            <div class="text-center powered">
              <h6 class="mt-4 mb-3">Powered By</h6>
              <a href="#">
                <img class="logo-lightmode" src="@/assets/img/logo.png" alt="Logo" />
                <img class="logo-darkmode" src="@/assets/img/logo-white.png" alt="Logo" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /View Modal -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
import Editor from "@tinymce/tinymce-vue";
export default {
  components: {
    editor: Editor,
  },

  data() {
    return {
      content: "Description",
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
      summernoteImageLinkInsert: null,
      Countrymodal: [
        "Select Country Name",
        "Country Name 1",
        "Country Name 2",
        "Country Name 3",
      ],
      State: ["Select State Name", "State Name 1", "State Name 2", "State Name 3"],
      Mode: ["Select Payment Mode", "Cash", "Cheque"],
      Status: ["Select Payment Status", "Paid", "Pending", "Cancelled"],
      Parent_Category1: ["None", "Coupons", "News", "Plugins", "Themes", "Tutorial"],
      Parent_Category: ["None", "Coupons", "News", "Plugins", "Themes", "Tutorial"],
      Status1: ["Select Status", "Active", "Inactive"],
      Role: ["Select Role", "Role 1", "Role 2"],
      Language: ["Select Language", "Tamil", "English"],
      Tax: ["N/A", "5%", "10%", "15%"],
    };
  },

  props: {
    title: {
      type: String,
      default: "",
    },
    Delete: {
      type: String,
      default: "",
    },
  },
};
</script>
