<template>
  <!-- View Companies Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="view_doamin"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div
            class="form-header modal-header-title text-start d-flex align-items-center mb-0"
          >
            <h4 class="mb-0">Domain Details</h4>
            <span class="badge bg-info-light ms-3">Pending</span>
          </div>
          <button
            type="button"
            class="btn-close ms-2"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
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
                    </div>
                  </div>
                  <div>
                    <span class="badge bg-success d-inline-flex align-items-center me-2"
                      ><i class="feather feather-check me-1"></i>Approve</span
                    >
                    <span class="badge bg-danger d-inline-flex align-items-center"
                      ><i class="feather feather-x me-1"></i>Reject</span
                    >
                  </div>
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
            <p>You want delete domain</p>
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
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
