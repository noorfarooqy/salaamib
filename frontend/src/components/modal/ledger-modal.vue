<template>
  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="#" class="sidebar-closes"><i class="fa-regular fa-circle-xmark"></i></a>
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
                  Name
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
                          <span class="checkmark"></span> John Smith
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Johnny charles
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Pricilla Maureen
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Randall Hollis
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Robert George
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Sharonda Letha
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

          <!-- Reference -->
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
                  Reference
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
                <div id="checkBoxes3">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689825
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689826
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689829
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689830
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689827
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 25689828
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Reference-->

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
                  Mode
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
                      <span class="checkmark"></span> Credit
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="payment-mode" />
                      <span class="checkmark"></span> Debit
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

  <!-- Add Ledger Modal -->
  <div class="modal custom-modal fade" id="add_ledger" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Ledger</h4>
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
                <label>Amount</label>
                <input type="text" class="form-control" placeholder="Enter Amount" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdate"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Reference</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Reference Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block d-inline-flex align-center mb-0">
                <label class="me-5 mb-0">Mode</label>
                <div>
                  <label class="custom_radio me-3 mb-0">
                    <input type="radio" name="payment" checked />
                    <span class="checkmark"></span> Credit
                  </label>
                  <label class="custom_radio mb-0">
                    <input type="radio" name="payment" />
                    <span class="checkmark"></span> Debit
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="#" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Ledger Modal -->

  <!-- Edit Ledger Modal -->
  <div class="modal custom-modal fade" id="edit_ledger" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Ledger</h4>
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
                <input type="text" class="form-control" placeholder="John Smith" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdateOne"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Reference</label>
                <input type="text" class="form-control" placeholder="25689826" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block d-inline-flex align-center mb-0">
                <label class="me-5 mb-0">Mode</label>
                <div>
                  <label class="custom_radio me-3 mb-0">
                    <input type="radio" name="payment" checked />
                    <span class="checkmark"></span> Credit
                  </label>
                  <label class="custom_radio mb-0">
                    <input type="radio" name="payment" />
                    <span class="checkmark"></span> Debit
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="#" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Ledger Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Ledger</h3>
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
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
    };
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
