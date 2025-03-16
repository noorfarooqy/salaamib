<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
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
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Grid-View"
              ><span><i class="feather feather-grid"></i></span>
            </a>
          </li>
          <li>
            <a class="active btn-filters" href="javascript:void(0);"
              ><span
                ><i
                  class="feather feather-list"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="List-View"
                ></i
              ></span>
            </a>
          </li>
          <li>
            <a
              class="btn btn-primary"
              href="javascript:void(0);"
              data-bs-toggle="modal"
              data-bs-target="#add_faq"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add FAQ</a
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- /Page Header -->
  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="javascript:;" class="sidebar-closes"
          ><i class="fa-regular fa-circle-xmark"></i
        ></a>
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
                  Customer
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
                          <span class="checkmark"></span> Brian Johnson
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Russell Copeland
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Greg Lynch
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> John Blair
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Barbara Moore
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Hendry Evan
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Richard Miles
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
                      v-model="startdateOne"
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
                      v-model="startdate"
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
          <div class="accordion" id="accordionMain3">
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
                  <div class="form-custom">
                    <input
                      type="text"
                      class="form-control"
                      id="member_search2"
                      placeholder="Search here"
                    />
                    <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                  </div>
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> All Invoices
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Paid
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Overdue
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Draft
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Recurring
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Cancelled
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Status -->

          <!-- Category -->
          <div class="accordion accordion-last" id="accordionMain4">
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
                <div id="checkBoxes3">
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
                      <span class="checkmark"></span> Repairs
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Software
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Two">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Stationary
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Medical
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Designing
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

          <button
            type="submit"
            class="d-inline-flex align-items-center justify-content-center btn w-100 btn-primary"
          >
            <span
              ><img
                src="@/assets/img/icons/chart.svg"
                class="me-2"
                alt="Generate report" /></span
            >Generate report
          </button>
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
    text: {
      type: String,
      default: "",
    },
    path: {
      type: Array,
      default: () => {
        return [];
      },
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
      for (var i = 0; i < popupToggleElements.length; i++) {
        popupToggleElements[i].addEventListener("click", function () {
          var toggleSidebar = document.getElementsByClassName("toggle-sidebar")[0];
          if (toggleSidebar) {
            toggleSidebar.classList.add("open-filter");
          }
        });
      }

      var sidebarClosesElements = document.getElementsByClassName("sidebar-closes");
      for (var j = 0; j < sidebarClosesElements.length; j++) {
        sidebarClosesElements[j].addEventListener("click", function () {
          var toggleSidebar = document.getElementsByClassName("toggle-sidebar")[0];
          if (toggleSidebar) {
            toggleSidebar.classList.remove("open-filter");
          }
        });
      }
    }

    function addViewAllFunctionality(className, buttonClass) {
      var elements = document.getElementsByClassName(className);
      var buttons = document.getElementsByClassName(buttonClass);

      if (elements.length > 0 && buttons.length > 0) {
        document.addEventListener("DOMContentLoaded", function () {
          for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "none";
          }

          for (var j = 0; j < buttons.length; j++) {
            buttons[j].addEventListener("click", function (event) {
              var buttonText = event.target.textContent;

              for (var k = 0; k < elements.length; k++) {
                elements[k].style.display =
                  elements[k].style.display === "none" ? "block" : "none";
              }

              event.target.textContent =
                buttonText === "Close All" ? "View All" : "Close All";
            });
          }
        });
      }
    }

    addViewAllFunctionality("viewall-One", "viewall-button-One");
    addViewAllFunctionality("viewall-Two", "viewall-button-Two");
    addViewAllFunctionality("viewall-Three", "viewall-button-Three");
  },
};
</script>
