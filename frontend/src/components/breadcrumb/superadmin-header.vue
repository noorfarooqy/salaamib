<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
      <div class="page-content">
        <div class="list-btn">
          <ul class="filter-list">
            <li>
              <a
                class="btn btn-filters w-auto popup-toggle"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Filter"
                ><span class="me-2"
                  ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
                >Filter
              </a>
            </li>

            <li>
              <div
                class="dropdown dropdown-action"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Download"
              >
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
              <a
                class="btn-filters"
                href="javascript:void(0);"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Print"
                ><span><i class="feather feather-printer"></i></span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

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
                  Companies
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
                          <span class="checkmark"></span> Orn LLC
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Accent Technology
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Express Advertising
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lexicon Technologies
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Sumo Soft Limited
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Repair Group Co
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

          <!-- Select Date -->
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
                  Select Date
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
                <div class="input-block mb-3">
                  <label class="form-control-label">From</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdate"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
                <div class="input-block mb-3">
                  <label class="form-control-label">To</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdateOne"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Select Date -->

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
                  By Status
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
                      <span class="checkmark"></span> Active
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Unsubscribed
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Awaiting Payment
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
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
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
