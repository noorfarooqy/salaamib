<template>
  <!-- Add Stock in Modal -->
  <div class="modal custom-modal fade" id="stock_in" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Stock in</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Name</label>
                <input
                  type="text"
                  class="bg-white-smoke form-control"
                  placeholder="SEO Service"
                />
              </div>
            </div>
            <div class="col-lg-6 col-md-12 mt-3">
              <div class="form-group">
                <label>Quantity</label>
                <input type="number" class="form-control" placeholder="0" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12 mt-3">
              <div class="form-group mb-0">
                <label>Units</label>
                <vue-select :options="Units" id="units" placeholder="Pieces" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-0">
                <label>Notes</label>
                <textarea
                  rows="3"
                  cols="3"
                  class="form-control"
                  placeholder="Enter Notes"
                ></textarea>
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
            >Add Quantity</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Stock in Modal -->

  <!-- Remove Stock Modal -->
  <div class="modal custom-modal fade" id="stock_out" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Remove Stock</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Name</label>
                <input
                  type="text"
                  class="bg-white-smoke form-control"
                  placeholder="SEO Service"
                />
              </div>
            </div>
            <div class="col-lg-6 col-md-12 mt-3">
              <div class="form-group">
                <label>Quantity</label>
                <input type="number" class="form-control" placeholder="0" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12 mt-3">
              <div class="form-group mb-0">
                <label>Units</label>
                <vue-select :options="Units1" id="units1" placeholder="Pieces" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-0">
                <label>Notes</label>
                <textarea
                  rows="3"
                  cols="3"
                  class="form-control"
                  placeholder="Enter Notes"
                ></textarea>
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
            >Remove Quantity</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Remove Stock Modal -->

  <!-- Edit Stock in Modal -->
  <div class="modal custom-modal fade" id="edit_inventory" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Inventory</h4>
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
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" value="Lorem ipsum dolor sit" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Code</label>
                <input type="text" class="form-control" value="P125389" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Units</label>
                <input type="text" class="form-control" value="Box" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Quantity</label>
                <input type="text" class="form-control" value="3" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Selling Price</label>
                <input type="text" class="form-control" value="$155.00" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-3">
                <label>Purchase Price</label>
                <input type="text" class="form-control" value="$150.00" />
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="input-block mb-0">
                <label>Status</label>
                <input type="text" class="form-control" value="Stock in" />
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
  <!-- /Edit Stock in Modal -->

  <!-- Delete Stock Modal -->
  <div class="modal custom-modal fade" id="delete_stock" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Inventory</h3>
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
  <!-- /Delete Stock Modal -->
</template>

<script>
export default {
  data() {
    return {
      Units: ["Pieces", "Inches", "Kilograms", "Inches", "Box"],
      Units1: ["Pieces", "Inches", "Kilograms", "Inches", "Box"],
    };
  },
};
</script>
