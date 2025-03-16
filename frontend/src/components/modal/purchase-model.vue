<template>
  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="javascript:;" class="sidebar-closes"><i class="fa-regular fa-circle-xmark"></i></a>
      </div>
      <div class="sidebar-body">
        <form action="javascript:;" autocomplete="off">
          <!-- Customer -->
          <div class="accordion" id="accordionMain1">
            <div class="card-header-new" id="headingOne">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  Supplier Name
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseOne"
              class="collapse show"
              aria-labelledby="headingOne"
              data-bs-parent="#accordionExample1"
            >
              <div class="card-body-chat">
                <div class="row">
                  <div class="col-md-12">
                    <div id="checkBoxes1">
                      <div class="form-custom">
                        <input
                          type="text"
                          class="form-control"
                          id="member_search1"
                          placeholder="Search Customer"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lenovo 3rd Generation
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Nike Jordan
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Apple Series 5 Watch
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Amazon Echo Dot
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Lobar Handy
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Woodcraft Sandal
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Black Slim 200
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Red Premium Handy
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Bold V3.2
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Iphone 14 Pro
                            </label>
                          </div>
                          <div class="view-all">
                            <a href="javascript:void(0);" class="viewall-button-One"
                              ><span class="me-2">View All</span
                              ><span><i class="fa fa-circle-chevron-down"></i></span
                            ></a>
                          </div>
                        </div>
                        <!-- /View All -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Customer -->

          <!-- Category -->
          <div class="accordion" id="accordionMain4">
            <div class="card-header-new" id="headingFour">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseFour"
                  aria-expanded="true"
                  aria-controls="collapseFour"
                >
                  Category
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseFour"
              class="collapse"
              aria-labelledby="headingFour"
              data-bs-parent="#accordionExample4"
            >
              <div class="card-body-chat">
                <div id="checkBoxes4">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Advertising
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Food
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Marketing
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Repairs
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Two">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Software
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Stationary
                        </label>
                      </div>
                      <div class="view-all">
                        <a href="javascript:void(0);" class="viewall-button-Two"
                          ><span class="me-2">View All</span
                          ><span><i class="fa fa-circle-chevron-down"></i></span
                        ></a>
                      </div>
                    </div>
                    <!-- /View All -->
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Category -->

          <!-- By Status -->
          <div class="accordion accordion-last" id="accordionMain3">
            <div class="card-header-new" id="headingThree">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseThree"
                  aria-expanded="true"
                  aria-controls="collapseThree"
                >
                  Payment Status
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseThree"
              class="collapse"
              aria-labelledby="headingThree"
              data-bs-parent="#accordionExample3"
            >
              <div class="card-body-chat">
                <div id="checkBoxes2">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Paid
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Pending
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Status -->

          <div class="filter-buttons">
            <button
              type="submit"
              class="d-inline-flex align-items-center justify-content-center btn w-100 btn-primary"
            >
              Apply
            </button>
            <button
              type="submit"
              class="d-inline-flex align-items-center justify-content-center btn w-100 btn-secondary"
            >
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!--/Add Asset -->

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
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
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
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Vendor</h3>
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
</template>
<script>
export default {
  data() {
    return {};
  },
  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      const popupToggleElements = document.getElementsByClassName("popup-toggle");
      const toggleSidebarElement = document.querySelector(".toggle-sidebar");
      const bodyElement = document.body;

      if (popupToggleElements.length > 0) {
        for (let i = 0; i < popupToggleElements.length; i++) {
          popupToggleElements[i].addEventListener("click", function () {
            toggleSidebarElement.classList.add("open-filter");
            bodyElement.classList.add("filter-opened");
          });
        }

        const sidebarCloseElements = document.getElementsByClassName("sidebar-closes");
        for (let i = 0; i < sidebarCloseElements.length; i++) {
          sidebarCloseElements[i].addEventListener("click", function () {
            toggleSidebarElement.classList.remove("open-filter");
            bodyElement.classList.remove("filter-opened");
          });
        }
      }
    });
    document.addEventListener("DOMContentLoaded", function () {
      function initializeViewAll(classPrefix) {
        var viewallOnes = document.getElementsByClassName("viewall-" + classPrefix);
        var viewallButton = document.getElementsByClassName(
          "viewall-button-" + classPrefix
        )[0];

        if (viewallOnes.length > 0 && viewallButton) {
          for (var i = 0; i < viewallOnes.length; i++) {
            viewallOnes[i].style.display = "none";
          }

          viewallButton.addEventListener("click", function () {
            var buttonText = viewallButton.textContent;
            for (var i = 0; i < viewallOnes.length; i++) {
              viewallOnes[i].style.display =
                viewallOnes[i].style.display === "none" ? "block" : "none";
            }

            viewallButton.textContent =
              buttonText === "Close All" ? "View All" : "Close All";
          });
        }
      }

      if (document.getElementsByClassName("viewall-One").length > 0) {
        initializeViewAll("One");
      }

      if (document.getElementsByClassName("viewall-Two").length > 0) {
        initializeViewAll("Two");
      }
    });
  },
};
</script>
