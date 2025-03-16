<template>
  <div class="modal custom-modal modal-lg fade" id="add_membership" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Membership</h4>
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
                <div class="form-group-add">
                  <h5 class="form-title">Plan</h5>
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Plan Name</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Plan Name"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Monthly Price</label>
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Enter Plan Price"
                        />
                        <span class="me-2 mt-2"
                          ><i class="feather feather-alert-circle"></i></span
                        ><span>Set 0 for free</span>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Yearly Price</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Yearly Price"
                        />
                        <span class="me-2"
                          ><i class="feather feather-alert-circle"></i></span
                        ><span>Set 0 for free</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group-add">
                  <h5 class="form-title">Plan Settings</h5>
                  <div class="row">
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Services</label>
                        <div class="align-center">
                          <input type="number" class="form-control" placeholder="1-100" />
                          <div class="status-toggle">
                            <input
                              id="rating_1"
                              class="check"
                              type="checkbox"
                              checked=""
                            />
                            <label for="rating_1" class="checktoggle checkbox-bg"
                              >checkbox</label
                            >
                          </div>
                        </div>
                        <span>
                          <label class="custom_check mt-2">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </span>
                        <span>Unlimited</span>
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Appointments</label>
                        <div class="align-center">
                          <input type="number" class="form-control" placeholder="1-100" />
                          <div class="status-toggle">
                            <input
                              id="rating_2"
                              class="check"
                              type="checkbox"
                              checked=""
                            />
                            <label for="rating_2" class="checktoggle checkbox-bg"
                              >checkbox</label
                            >
                          </div>
                        </div>
                        <span>
                          <label class="custom_check mt-2">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                            <span>Unlimited</span>
                          </label>
                        </span>
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Staffs</label>
                        <div class="align-center">
                          <input type="number" class="form-control" placeholder="1-100" />
                          <div class="status-toggle">
                            <input
                              id="rating_3"
                              class="check"
                              type="checkbox"
                              checked=""
                            />
                            <label for="rating_3" class="checktoggle checkbox-bg"
                              >checkbox</label
                            >
                          </div>
                        </div>
                        <span>
                          <label class="custom_check mt-2">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                            <span>Unlimited</span>
                          </label>
                        </span>
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Gallery</label>
                        <div class="align-center">
                          <input type="number" class="form-control" placeholder="1-100" />
                          <div class="status-toggle">
                            <input
                              id="rating_4"
                              class="check"
                              type="checkbox"
                              checked=""
                            />
                            <label for="rating_4" class="checktoggle checkbox-bg"
                              >checkbox</label
                            >
                          </div>
                        </div>
                        <span>
                          <label class="custom_check mt-2">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                            <span>Unlimited</span>
                          </label>
                        </span>
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Additional Service</label>
                        <div class="align-center">
                          <input type="number" class="form-control" placeholder="1-100" />
                          <div class="status-toggle">
                            <input
                              id="rating_5"
                              class="check"
                              type="checkbox"
                              checked=""
                            />
                            <label for="rating_5" class="checktoggle checkbox-bg"
                              >checkbox</label
                            >
                          </div>
                        </div>
                        <span>
                          <label class="custom_check mt-2">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                            <span>Unlimited</span>
                          </label>
                        </span>
                      </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-12">
                      <div class="form-group booking-option">
                        <label>Booking Option</label>
                        <div class="status-toggle">
                          <input id="rating_6" class="check" type="checkbox" checked="" />
                          <label for="rating_6" class="checktoggle checkbox-bg"
                            >checkbox</label
                          >
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
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add Plan</a
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
