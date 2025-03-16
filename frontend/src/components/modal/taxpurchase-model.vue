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
                          placeholder="Search here"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Michael
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Richard
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Joseph
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> David
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Benjamin
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Steven
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

          <!-- Product Code -->
          <div class="accordion" id="accordionMain2">
            <div class="card-header-new" id="headingTwo">
              <h6 class="filter-title">
                <a
                  href="javascript:void(0);"
                  class="w-100 collapsed"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseTwo"
                  aria-expanded="true"
                  aria-controls="collapseTwo"
                >
                  Ref No
                  <span class="float-end"><i class="fa-solid fa-chevron-down"></i></span>
                </a>
              </h6>
            </div>

            <div
              id="collapseTwo"
              class="collapse"
              aria-labelledby="headingTwo"
              data-bs-parent="#accordionExample2"
            >
              <div class="card-body-chat">
                <div id="checkBoxes3">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="ref-no" />
                      <span class="checkmark"></span> 312345
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="ref-no" />
                      <span class="checkmark"></span> 236348
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="ref-no" />
                      <span class="checkmark"></span> 395374
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="ref-no" />
                      <span class="checkmark"></span> 763265
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Two">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="ref-no" />
                          <span class="checkmark"></span> 893246
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="ref-no" />
                          <span class="checkmark"></span> 457289
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
          <!-- /Product Code -->

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
                  Payment Method
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
                      <input type="checkbox" name="payment-mode" />
                      <span class="checkmark"></span> Cash
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="payment-mode" />
                      <span class="checkmark"></span> Cheque
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

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Companies</h3>
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

  <!-- Add Package Modal -->
  <div class="modal custom-modal fade p-20" id="add_package" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Package</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <h6>Plan Type</h6>
          <ul class="nav nav-tabs row" id="myTab" role="tablist">
            <li class="nav-item col-md-4 text-center" role="presentation">
              <h6
                class="nav-link active"
                id="month-tab"
                data-bs-toggle="tab"
                data-bs-target="#month"
                role="tab"
                aria-controls="month"
                aria-selected="true"
              >
                Monthly
              </h6>
            </li>
            <li class="nav-item col-md-4 text-center" role="presentation">
              <h6
                class="nav-link"
                id="year-tab"
                data-bs-toggle="tab"
                data-bs-target="#year"
                role="tab"
                aria-controls="year"
                aria-selected="false"
              >
                Yearly
              </h6>
            </li>
            <li class="nav-item col-md-4 text-center" role="presentation">
              <h6
                class="nav-link"
                id="lifetime-tab"
                data-bs-toggle="tab"
                data-bs-target="#lifetime"
                role="tab"
                aria-controls="lifetime"
                aria-selected="false"
              >
                Lifetime
              </h6>
            </li>
          </ul>
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="month"
              role="tabpanel"
              aria-labelledby="month-tab"
            >
              <div class="form-check">
                <label class="form-check-label" for="monthly1">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="monthly"
                    id="monthly1"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Basic</span>
                    <span >$49.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="monthly2">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="monthly"
                    id="monthly2"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Enterprise</span>
                    <span >$99.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="monthly3">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="monthly"
                    id="monthly3"
                    checked
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Free Trail</span>
                    <span >$0.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
            </div>
            <div
              class="tab-pane fade"
              id="year"
              role="tabpanel"
              aria-labelledby="year-tab"
            >
              <div class="form-check">
                <label class="form-check-label" for="yearly1">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="yearly"
                    id="yearly1"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Basic</span>
                    <span >$49.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="yearly2">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="yearly"
                    id="yearly2"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Enterprise</span>
                    <span >$99.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="yearly3">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="yearly"
                    id="yearly3"
                    checked
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Free Trail</span>
                    <span >$0.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
            </div>
            <div
              class="tab-pane fade"
              id="lifetime"
              role="tabpanel"
              aria-labelledby="lifetime-tab"
            >
              <div class="form-check">
                <label class="form-check-label" for="lifetime1">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="lifetime"
                    id="lifetime1"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Basic</span>
                    <span >$49.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="lifetime2">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="lifetime"
                    id="lifetime2"
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Enterprise</span>
                    <span >$99.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
              <div class="form-check">
                <label class="form-check-label" for="lifetime3">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="lifetime"
                    id="lifetime3"
                    checked
                  />
                  <span class="d-flex justify-content-between text-dark">
                    <span >Free Trail</span>
                    <span >$0.00</span>
                  </span>
                  <span class="d-flex justify-content-between text-dull">
                    <span >Lorem Ipsum is simply dummy text</span>
                    <span >/month</span>
                  </span>
                </label>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Assign</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Package Modal -->
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
