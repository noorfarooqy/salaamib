<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
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
                <h5>Payment Settings</h5>
              </div>
              <div class="form-group-item">
                <div class="row">
                  <div class="col-12">
                    <div class="payment-toggle">
                      <h5 class="form-title">Strip</h5>
                      <div class="status-toggle">
                        <input id="rating_1" class="check" type="checkbox" checked="" />
                        <label for="rating_1" class="checktoggle checkbox-bg">checkbox</label>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6 col-12">
                    <div class="form-group">
                      <label>Stripe Key</label>
                      <input type="text" class="form-control" placeholder="Enter Stripe Key" />
                    </div>
                  </div>
                  <div class="col-lg-6 col-12">
                    <div class="form-group">
                      <label>Stripe Secret</label>
                      <input type="text" class="form-control" placeholder="Enter Stripe Secret" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-group-item">
                <div class="row">
                  <div class="col-12">
                    <div class="payment-toggle">
                      <h5 class="form-title">Paypal</h5>
                      <div class="status-toggle">
                        <input id="rating_2" class="check" type="checkbox" checked="" />
                        <label for="rating_2" class="checktoggle checkbox-bg">checkbox</label>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-12">
                    <div class="form-group">
                      <label>Paypal Client Id</label>
                      <input type="text" class="form-control" placeholder="Enter Paypal Client Id" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-12">
                    <div class="form-group">
                      <label>Paypal Secret</label>
                      <input type="text" class="form-control" placeholder="Enter Paypal Secret" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-12">
                    <div class="form-group">
                      <label>Paypal Mode</label>
                      <vue-select :options="Mode" id="mode" placeholder="Select Paypal Mode" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-group-item border-0 p-0">
                <div class="row">
                  <div class="col-12">
                    <div class="payment-toggle">
                      <h5 class="form-title">Razorpay</h5>
                      <div class="status-toggle">
                        <input id="rating_3" class="check" type="checkbox" checked="" />
                        <label for="rating_3" class="checktoggle checkbox-bg">checkbox</label>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6 col-12">
                    <div class="form-group mb-0">
                      <label>Razorpay Key Id</label>
                      <input type="text" class="form-control" placeholder="Enter Razorpay Key Id" />
                    </div>
                  </div>
                  <div class="col-lg-6 col-12">
                    <div class="form-group mb-0">
                      <label>Razorpay Secret</label>
                      <input type="text" class="form-control" placeholder="Enter Razorpay Secret" />
                    </div>
                  </div>
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
    <!-- /Page Wrapper -->
  </div>
</template>
<script>
export default {
  setup() {
    return {
      Mode: ["Select Paypal Mode", "Debit Card", "Credit Card"],
    };
  },
};
</script>
