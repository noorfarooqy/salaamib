<template>
  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Account Details</h3>
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

  <!-- Add Tax & Discount Modal -->
  <div class="modal custom-modal fade" id="add_discount" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Tax</h4>
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
                <label>Tax Name</label>
                <input
                  type="number"
                  class="form-control mb-3"
                  placeholder="Enter Tax Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Tax Rates</label>
                <input
                  type="text"
                  class="form-control mb-3"
                  placeholder="Enter Tax Rates"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Type</label>
                <vue-select :options="Type" id="Type" placeholder="Select Type" />
              </div>
            </div>
            <div class="payment-toggle">
              <h5 class="form-title">Status</h5>
              <div class="status-toggle">
                <input id="rating_7" class="check" type="checkbox" checked="" />
                <label for="rating_7" class="checktoggle checkbox-bg">checkbox</label>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer add-tax-btns">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn add-btn-cancel-btn">Cancel</a>
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary add-tax-save-btn"
            >Save</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Tax & Discount Modal -->
</template>
<script>
export default {
  data() {
    return {
      Type: ["Select Type", "Percentage", "Fixed"],
    };
  },
};
</script>
