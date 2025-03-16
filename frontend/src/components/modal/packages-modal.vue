<template>
  <!-- Add New Package Modal -->
  <div class="modal custom-modal fade p-20" id="add_newpackage" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add New</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form action="#">
          <div class="modal-body">
            <h5 class="form-title">Plan Image</h5>
            <div class="row">
              <div class="col-md-12">
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
              <div class="col-md-12">
                <h5 class="form-title mb-3">Plan Info</h5>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Plan Name"
                    value=""
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Type</label>
                  <vue-select :options="MonthPack" id="packmonth" placeholder="Monthly" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Position</label>
                  <vue-select :options="NumPack" id="packnum" placeholder="1" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Currency</label>
                  <vue-select :options="USDPack" id="packusd" placeholder="USD" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label class="d-flex justify-content-between">
                    <span>Price</span>
                    <span class="text-primary"
                      ><i class="fa-solid fa-circle-exclamation me-2"></i>Set 0 for
                      free</span
                    >
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Package Price"
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-3">
                <div class="input-block mb-3">
                  <label>Discount Type</label>
                  <vue-select :options="FixedPack" id="packfixed" placeholder="Fixed" />
                </div>
              </div>
              <div class="col-sm-12 col-md-3">
                <div class="input-block mb-3">
                  <label>Discount</label>
                  <input type="text" class="form-control" placeholder="Enter Discount" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Limitations Invoices</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Max Customers</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Product</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Supplier</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
            </div>
            <h6>Plan Modules</h6>
            <div class="input-block mb-3">
              <div class="row">
                <div class="col-lg-12">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Select All
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Invoices
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Payments
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Payment Summary
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Vendors
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Estimates
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Quotations
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Memberships
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Customers
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Recurring Invoices
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Delivery Challans
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Products
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Vendors
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Expenses
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Reports
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Inventory
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Signature
                    </label>
                  </div>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <h6 class="mb-0">Access Trial</h6>
              <div class="status-toggle">
                <input id="access-trail-2" class="check" type="checkbox" checked="" />
                <label for="access-trail-2" class="checktoggle checkbox-bg"
                  >checkbox</label
                >
              </div>
            </div>
            <div class="row align-items-center">
              <div class="col-sm-12 col-md-8">
                <div class="input-block mb-3">
                  <label>Trial Days</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
              <div class="col-md-4">
                <div class="d-flex align-items-center mb-3">
                  <h6 class="mb-0">Is Recommended</h6>
                  <div class="status-toggle">
                    <input id="recommended" class="check" type="checkbox" />
                    <label for="recommended" class="checktoggle checkbox-bg"
                      >checkbox</label
                    >
                  </div>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-12">
                <div class="input-block mb-3">
                  <label>Description</label>
                  <textarea
                    rows="3"
                    cols="5"
                    class="form-control"
                    placeholder="Enter Description"
                  ></textarea>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <h6 class="mb-0">Status</h6>
              <div class="status-toggle">
                <input id="status" class="check" type="checkbox" />
                <label for="status" class="checktoggle checkbox-bg">checkbox</label>
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
  <!-- /Add New Package Modal -->

  <!-- Edit Package Modal -->
  <div
    class="modal custom-modal custom-lg-modal fade p-20"
    id="edit_package"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Package</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form action="#">
          <div class="modal-body">
            <h5 class="form-title">Plan Image</h5>
            <div class="row">
              <div class="col-md-12">
                <div class="profile-picture">
                  <div class="upload-profile">
                    <div class="profile-img company-profile-img">
                      <img
                        id="company-img-2"
                        class="img-fluid me-0"
                        src="@/assets/img/icons/price-02.svg"
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
              <div class="col-md-12">
                <h5 class="form-title mb-3">Plan Info</h5>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Plan Name"
                    value="Enterprise"
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Type</label>
                  <vue-select
                    :options="MonthlyPlan"
                    id="monthlyplan"
                    placeholder="Monthly"
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Position</label>
                  <vue-select :oprion="NumberPlan" id="numberplan" placeholder="1" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label>Plan Currency</label>
                  <vue-select :options="USDPlan" id="usdplan" placeholder="USD" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6">
                <div class="input-block mb-3">
                  <label class="d-flex justify-content-between">
                    <span>Price</span>
                    <span class="text-primary"
                      ><i class="fa-solid fa-circle-exclamation me-2"></i>Set 0 for
                      free</span
                    >
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Package Price"
                    value="4545"
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-3">
                <div class="input-block mb-3">
                  <label>Discount Type</label>
                  <vue-select :options="FixedPlan" id="fixedplan" placeholder="Fixed" />
                </div>
              </div>
              <div class="col-sm-12 col-md-3">
                <div class="input-block mb-3">
                  <label>Discount</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Discount"
                    value="5%"
                  />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Limitations Invoices</label>
                  <input type="number" class="form-control" placeholder="0" value="50" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Max Customers</label>
                  <input type="number" class="form-control" placeholder="0" value="250" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Product</label>
                  <input type="number" class="form-control" placeholder="0" value="110" />
                </div>
              </div>
              <div class="col-sm-12 col-md-6 col-lg-3">
                <div class="input-block mb-3">
                  <label>Supplier</label>
                  <input type="number" class="form-control" placeholder="0" value="14" />
                </div>
              </div>
            </div>
            <h6>Plan Modules</h6>
            <div class="input-block mb-3">
              <div class="row">
                <div class="col-lg-12">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Select All
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Invoices
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Payments
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Payment Summary
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Vendors
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Estimates
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Quotations
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Memberships
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Customers
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Recurring Invoices
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Delivery Challans
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Products
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Vendors
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Expenses
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Reports
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked /> Inventory
                    </label>
                  </div>
                </div>
                <div class="col-lg-3 col-sm-6">
                  <div class="checkboxes">
                    <label>
                      <input type="checkbox" name="checkbox" checked />Signature
                    </label>
                  </div>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <h6 class="mb-0">Access Trial</h6>
              <div class="status-toggle">
                <input id="access-trail" class="check" type="checkbox" checked="" />
                <label for="access-trail" class="checktoggle checkbox-bg">checkbox</label>
              </div>
            </div>
            <div class="row align-items-center">
              <div class="col-sm-12 col-md-8">
                <div class="input-block mb-3">
                  <label>Trial Days</label>
                  <input type="number" class="form-control" placeholder="0" />
                </div>
              </div>
              <div class="col-md-4">
                <div class="d-flex align-items-center mb-3">
                  <h6 class="mb-0">Is Recommended</h6>
                  <div class="status-toggle">
                    <input id="recommended-2" class="check" type="checkbox" />
                    <label for="recommended-2" class="checktoggle checkbox-bg"
                      >checkbox</label
                    >
                  </div>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-12">
                <div class="input-block mb-3">
                  <label>Description</label>
                  <textarea
                    rows="3"
                    cols="5"
                    class="form-control"
                    placeholder="Enter Description"
                  ></textarea>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <h6 class="mb-0">Status</h6>
              <div class="status-toggle">
                <input id="status-2" class="check" type="checkbox" />
                <label for="status-2" class="checktoggle checkbox-bg">checkbox</label>
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
  <!-- /Edit Package Modal -->

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
            <p>You want delete plan</p>
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
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  data() {
    return {
      FixedPlan: ["Fixed", "Percentage"],
      NumberPlan: ["1", "2", "3"],
      USDPlan: ["USD", "$"],
      MonthlyPlan: ["Monthly", "Yearly", "Lifetime"],
      FixedPack: ["Fixed", "Percentage"],
      USDPack: ["USD", "$"],
      NumPack: ["1", "2", "3"],
      MonthPack: ["Monthly", "Yearly", "Lifetime"],
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
    };
  },
};
</script>
