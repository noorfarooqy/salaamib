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
                <h5>Email Settings</h5>
              </div>
              <div class="row">
                <h5 class="mail-title">mail Provider</h5>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <div class="mail-provider">
                      <h4>PHP Mail</h4>
                      <div class="mail-setting">
                        <a
                          href="javascript:;"
                          data-bs-toggle="modal"
                          data-bs-target="#bank_details"
                          ><i class="feather feather-settings"></i
                        ></a>
                        <div class="status-toggle">
                          <input id="rating_1" class="check" type="checkbox" checked="" />
                          <label for="rating_1" class="checktoggle checkbox-bg"
                            >checkbox</label
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <div class="mail-provider">
                      <h4>SMTP</h4>
                      <div class="mail-setting">
                        <a href="javascript:;"
                          ><i class="feather feather-settings"></i
                        ></a>
                        <div class="status-toggle">
                          <input id="rating_2" class="check" type="checkbox" checked="" />
                          <label for="rating_2" class="checktoggle checkbox-bg"
                            >checkbox</label
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Email From Name</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Email From Name"
                    />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Email From Address</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Email From Address"
                    />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Email Global Footer</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Email Global Footer"
                    />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Send Test Email</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Email Address"
                    />
                  </div>
                </div>
                <div class="col-lg-12">
                  <div class="btn-path text-end">
                    <a
                      href="javascript:void(0);"
                      class="btn btn-cancel bg-primary-light me-3"
                      >Cancel</a
                    >
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
  <!-- PHP Mail Modal -->
  <div class="modal custom-modal fade" id="bank_details" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title php-mail-modal text-start mb-0">
            <h4 class="mb-0">PHP Mail</h4>
            <div class="status-toggle">
              <input id="rating_3" class="check" type="checkbox" checked="" />
              <label for="rating_3" class="checktoggle checkbox-bg">checkbox</label>
            </div>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Email From Address</label>
                <input type="text" class="form-control" placeholder="demo2" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Email Password</label>
                <input type="password" class="form-control" placeholder="*******" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Email From Name</label>
                <input type="text" class="form-control" placeholder="John Smith" />
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
            >Save</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /PHP Mail Modal -->
</template>
<script>
export default {
  setup() {
    return {};
  },
};
</script>
