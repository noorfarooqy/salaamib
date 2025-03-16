<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- /Page Header -->
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar></settingsidebar>
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header">
                <h5>SAAS Settings</h5>
              </div>
              <form action="#">
                <div class="row">
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Select Default Currency</label>
                      <vue-select
                        :options="UnitedSel"
                        id="unitedsel"
                        placeholder="United States Dollar ( USD )"
                      />
                    </div>
                  </div>
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Days between initial warning and subscription ends</label>
                      <input type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Interval days between warnings</label>
                      <input type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Interval days between warnings</label>
                      <input type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Maximum Free Domain A Subscriber Can Create</label>
                      <input type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="payment-toggle">
                      <h5 class="form-title">Email Verification</h5>
                      <div class="status-toggle">
                        <input id="rating_1" class="check" type="checkbox" checked="" />
                        <label for="rating_1" class="checktoggle checkbox-bg"
                          >checkbox</label
                        >
                      </div>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="payment-toggle">
                      <h5 class="form-title">Auto approve Domain creation request</h5>
                      <div class="status-toggle">
                        <input id="rating_2" class="check" type="checkbox" checked="" />
                        <label for="rating_2" class="checktoggle checkbox-bg"
                          >checkbox</label
                        >
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="modal-footer p-0">
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
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- /Page Wrapper -->
    </div>
  </div>
  <saas-settings-modal></saas-settings-modal>
</template>
<script>
export default {
  data() {
    return {
      UnitedSel: ["United States Dollar ( USD )", "Euro (€)", "Japanese Yen (¥)"],
    };
  },
};
</script>
