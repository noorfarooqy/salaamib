<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>Customers</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li>
            <a class="btn btn-filters w-auto popup-toggle"
              ><span class="me-2"
                ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
              >Filter
            </a>
          </li>
          <li>
            <div class="dropdown dropdown-action">
              <a
                href="javascript:;"
                class="btn-filters"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                ><span><i class="feather feather-download"></i></span
              ></a>
              <div class="dropdown-menu dropdown-menu-end">
                <ul class="d-block">
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-pdf me-2"></i>PDF</a
                    >
                  </li>
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-text me-2"></i>CVS</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <a class="btn-filters" href="javascript:void(0);"
              ><span><i class="feather feather-printer"></i></span>
            </a>
          </li>
          <li>
            <a class="btn btn-import" href="javascript:void(0);"
              ><span
                ><i class="feather feather-check-square me-2"></i>Import Customer</span
              ></a
            >
          </li>
          <li>
            <router-link class="btn btn-primary" to="/customers/add-customer"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add
              Customer</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- /Page Header -->

  <!-- Add Asset -->
  <div class="toggle-sidebar ledge">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header ledge">
        <h5>PayIn</h5>
        <a href="javascript:;" class="sidebar-closes"
          ><i class="fa-regular fa-circle-xmark"></i
        ></a>
      </div>
      <div class="sidebar-header submenu">
        <h6>Test Company</h6>
        <p class="text-success-light">Balance: $400</p>
      </div>
      <div class="sidebar-body">
        <form action="javascript:;" autocomplete="off">
          <!-- Customer -->
          <div class="accordion accordion-last" id="accordionMain1">
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
                  Customers
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
                          <span class="checkmark"></span> John Smith
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Johnny Charles
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Robert George
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Sharonda Letha
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Pricilla Maureen
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Randall Hollis
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
          <div class="accordion" id="accordionMain2">
            <div class="col-lg-12 col-sm-12">
              <div class="input-block mb-3">
                <label>Enter Amount</label>
                <input type="text" class="form-control" placeholder="Enter Amount" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Payment Date</label>
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
            <div class="input-block mb-3 notes-form-group-info">
              <label>Notes</label>
              <textarea class="form-control" placeholder="Enter your notes"></textarea>
            </div>
            <div class="modal-footer">
              <a href="javascript:;" class="btn btn-back cancel-btn me-2">Cancel</a>
              <a href="javascript:;" class="btn btn-primary paid-continue-btn"
                >Add Payment</a
              >
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!--/Add Asset -->
</template>

<script>
import { ref } from "vue";
const currentDate = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
    };
  },
  mounted() {
    var popupToggleElements = document.getElementsByClassName("popup-toggle");
    if (popupToggleElements.length > 0) {
      Array.from(popupToggleElements).forEach(function (el) {
        el.addEventListener("click", function () {
          document
            .getElementsByClassName("toggle-sidebar")[0]
            .classList.add("open-filter");
        });
      });

      var sidebarCloseElements = document.getElementsByClassName("sidebar-closes");
      Array.from(sidebarCloseElements).forEach(function (el) {
        el.addEventListener("click", function () {
          document
            .getElementsByClassName("toggle-sidebar")[0]
            .classList.remove("open-filter");
        });
      });
    }

    var viewallOneElements = document.getElementsByClassName("viewall-One");
    if (viewallOneElements.length > 0) {
      document.addEventListener("DOMContentLoaded", function () {
        Array.from(viewallOneElements).forEach(function (element) {
          element.style.display = "none";
        });

        var viewallButton = document.getElementsByClassName("viewall-button-One")[0];
        viewallButton.addEventListener("click", function () {
          var buttonText = viewallButton.textContent;
          Array.from(viewallOneElements).forEach(function (element) {
            element.style.display = element.style.display === "none" ? "block" : "none";
          });

          viewallButton.textContent =
            buttonText === "Close All" ? "View All" : "Close All";
        });
      });
    }
  },
};
</script>
