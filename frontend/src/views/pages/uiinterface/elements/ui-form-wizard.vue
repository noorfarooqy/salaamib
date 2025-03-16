<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <element-breadcrumb :title="title" />
      <div class="row">
        <!-- Lightbox -->
        <div class="col-lg-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title mb-0">Basic Wizard</h4>
            </div>
            <div class="card-body">
              <div class="wizard">
                <ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
                  <li class="nav-item flex-fill" role="presentation" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Seller Details">
                    <a class="nav-link active rounded-circle mx-auto d-flex align-items-center justify-content-center"
                      href="#step1" id="step1-tab" data-bs-toggle="tab" role="tab" aria-controls="step1"
                      aria-selected="true">
                      <i class="far fa-user"></i>
                    </a>
                  </li>
                  <li class="nav-item flex-fill" role="presentation" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Company Document">
                    <a class="nav-link rounded-circle mx-auto d-flex align-items-center justify-content-center"
                      href="#step2" id="step2-tab" data-bs-toggle="tab" role="tab" aria-controls="step2"
                      aria-selected="false">
                      <i class="fas fa-map-pin"></i>
                    </a>
                  </li>
                  <li class="nav-item flex-fill" role="presentation" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Bank Details">
                    <a class="nav-link rounded-circle mx-auto d-flex align-items-center justify-content-center"
                      href="#step3" id="step3-tab" data-bs-toggle="tab" role="tab" aria-controls="step3"
                      aria-selected="false">
                      <i class="fas fa-credit-card"></i>
                    </a>
                  </li>
                </ul>
                <div class="tab-content" id="myTabContent">
                  <div class="tab-pane fade show active" role="tabpanel" id="step1" aria-labelledby="step1-tab">
                    <div class="mb-4">
                      <h5>Enter Your Personal Details</h5>
                    </div>
                    <b-form>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-firstname-input" class="form-label">First name</label>
                            <b-form-input type="text" class="form-control" id="basicpill-firstname-input" />
                          </div>
                        </div>
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-lastname-input" class="form-label">Last name</label>
                            <b-form-input type="text" class="form-control" id="basicpill-lastname-input" />
                          </div>
                        </div>
                      </div>

                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-phoneno-input" class="form-label">Phone</label>
                            <b-form-input type="text" class="form-control" id="basicpill-phoneno-input" />
                          </div>
                        </div>
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-email-input" class="form-label">Email</label>
                            <b-form-input type="email" class="form-control" id="basicpill-email-input" />
                          </div>
                        </div>
                      </div>
                    </b-form>
                    <div class="d-flex">
                      <a class="btn btn btn-primary next">Next</a>
                    </div>
                  </div>
                  <div class="tab-pane fade" role="tabpanel" id="step2" aria-labelledby="step2-tab">
                    <div class="mb-4">
                      <h5>Enter Your Address</h5>
                    </div>
                    <b-form>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-pancard-input" class="form-label">Address 1</label>
                            <b-form-input type="text" class="form-control" id="basicpill-pancard-input" />
                          </div>
                        </div>

                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-vatno-input" class="form-label">Address 2</label>
                            <b-form-input type="text" class="form-control" id="basicpill-vatno-input" />
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-cstno-input" class="form-label">Landmark</label>
                            <b-form-input type="text" class="form-control" id="basicpill-cstno-input" />
                          </div>
                        </div>

                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-servicetax-input" class="form-label">Town</label>
                            <b-form-input type="text" class="form-control" id="basicpill-servicetax-input" />
                          </div>
                        </div>
                      </div>
                    </b-form>
                    <div class="d-flex">
                      <a class="btn btn btn-primary previous me-2"> Back</a>
                      <a class="btn btn btn-primary next">Continue</a>
                    </div>
                  </div>
                  <div class="tab-pane fade" role="tabpanel" id="step3" aria-labelledby="step3-tab">
                    <div class="mb-4">
                      <h5>Payment Details</h5>
                    </div>
                    <b-form>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-namecard-input" class="form-label">Name on Card</label>
                            <b-form-input type="text" class="form-control" id="basicpill-namecard-input" />
                          </div>
                        </div>

                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label>Credit Card Type</label>
                            <vue-select :options="type" id="Credit-Card" placeholder="Select Card Type" />
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-cardno-input" class="form-label">Credit Card Number</label>
                            <b-form-input type="text" class="form-control" id="basicpill-cardno-input" />
                          </div>
                        </div>

                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-card-verification-input" class="form-label">Card Verification
                              Number</label>
                            <b-form-input type="text" class="form-control" id="basicpill-card-verification-input" />
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="input-block mb-3">
                            <label for="basicpill-expiration-input" class="form-label">Expiration Date</label>
                            <b-form-input type="text" class="form-control" id="basicpill-expiration-input" />
                          </div>
                        </div>
                      </div>
                    </b-form>
                    <div class="d-flex">
                      <a class="btn btn-primary previous me-2">Previous</a>
                      <a class="btn btn-primary next" data-bs-toggle="modal" data-bs-target="#save_modal">Save
                        Changes</a>
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
  <!-- /Page Wrapper -->
  <!-- Modal -->
  <div class="modal fade confirmModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content p-3">
        <div class="modal-header border-bottom-0">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="text-center">
            <h5 class="mb-3">Confirm Save Changes</h5>
            <button type="button" class="btn btn-dark w-md me-1" data-bs-dismiss="modal">
              Close
            </button>
            <button type="button" class="btn btn-primary w-md" data-bs-dismiss="modal">
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      type: ["American Express", "Visa", "MasterCard", "Discover"],
      title: "Form Wizard",
    };
  },
  mounted() { },
};
</script>
