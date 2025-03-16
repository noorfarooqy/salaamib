<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Pages list</h5>
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
                <a class="btn-filters" href="javascript:void(0);"
                  ><span><i class="feather feather-settings"></i></span>
                </a>
              </li>
              <li>
                <a class="btn-filters" href="javascript:void(0);"
                  ><span><i class="feather feather-grid"></i></span>
                </a>
              </li>
              <li>
                <a class="active btn-filters" href="javascript:void(0);"
                  ><span><i class="feather feather-list"></i></span>
                </a>
              </li>
              <li>
                <a class="btn btn-primary" href="javascript:;"
                  ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Pages</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- /Page Header -->

      <div class="row">
        <div class="col-md-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table
                  class="stripped table-hover"
                  :columns="columns"
                  :data-source="data"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Visibility'">
                      <div>{{ record.Visibility }}</div>
                    </template>
                    <template v-else-if="column.key === 'Date'">
                      <div class="status-toggle">
                        <input id="rating_1" class="check" type="checkbox" checked />
                        <label for="rating_1" class="checktoggle checkbox-bg">{{
                          record.Date
                        }}</label>
                      </div>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a
                          href="javascript:;"
                          class="btn-action-icon me-2"
                          data-bs-toggle="modal"
                          data-bs-target="#pages_edit"
                          ><span><i class="feather feather-edit"></i></span
                        ></a>
                        <a
                          href="javascript:;"
                          class="btn-action-icon"
                          data-bs-toggle="modal"
                          data-bs-target="#page_delete"
                          ><span><i class="feather feather-trash-2"></i></span
                        ></a>
                      </div>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->

  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="javascript:;" class="sidebar-closes"
          ><i class="fa-regular fa-circle-xmark"></i
        ></a>
      </div>
      <div class="sidebar-body">
        <b-form action="javascript:;" autocomplete="off">
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
                        <b-form-input
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
                <div class="form-group">
                  <label class="form-control-label">From</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdate"
                      type="email"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                      placeholder="DD-MM-YYYY"
                    />
                  </div>
                </div>
                <div class="form-group">
                  <label class="form-control-label">To</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdate1"
                      type="email"
                      class="datetimepicker form-control"
                      :editable="true"
                      :clearable="false"
                      :input-format="dateFormat"
                      placeholder="DD-MM-YYYY"
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
                    <b-form-input
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
        </b-form>
      </div>
    </div>
  </div>

  <div class="modal custom-modal fade" id="pages_edit" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header">
          <div class="form-header text-start mb-0">
            <h4 class="mb-0 text-dark fw-bold">Edit About Us</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Page Title(English)</label>
                <input type="text" class="form-control" placeholder="About Us" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Page Slug</label>
                <input type="text" class="form-control" placeholder="about-us" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Page Content(English)</label>
                <textarea
                  rows="5"
                  cols="5"
                  class="form-control"
                  placeholder="about us page contents"
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
            >Back</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Save</a
          >
        </div>
      </div>
    </div>
  </div>

  <div class="modal custom-modal fade" id="page_delete" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Pages list</h3>
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
</template>

<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDate1 = ref(new Date());
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Pages",
    dataIndex: "Pages",
    sorter: {
      compare: (a, b) => {
        a = a.Pages.toLowerCase();
        b = b.Pages.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "language",
    dataIndex: "language",
    key: "language",
    sorter: {
      compare: (a, b) => {
        a = a.language.toLowerCase();
        b = b.language.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Location",
    dataIndex: "Location",
    key: "Location",
    sorter: {
      compare: (a, b) => {
        a = a.Location.toLowerCase();
        b = b.Location.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Visibility",
    dataIndex: "Visibility",
    sorter: {
      compare: (a, b) => {
        a = a.Visibility.toLowerCase();
        b = b.Visibility.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Date",
    dataIndex: "Date",
    key: "Date",
    sorter: {
      compare: (a, b) => {
        a = a.Date.toLowerCase();
        b = b.Date.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    Pages: "Shops",
    language: "English",
    Location: "Quick Links",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
  {
    NUM: "2",
    Pages: "Blog",
    language: "English",
    Location: "Top Menu",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
  {
    NUM: "3",
    Pages: "Contact",
    language: "English",
    Location: "Quick Links",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
  {
    NUM: "4",
    Pages: "About Us",
    language: "English",
    Location: "Top Menu",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
  {
    NUM: "5",
    Pages: "Home",
    language: "English",
    Location: "Top Menu",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
  {
    NUM: "6",
    Pages: "FAQ",
    language: "English",
    Location: "Quick Links",
    Visibility: "19 Dec 2023, 06:12 PM",
    Date: "checkbox",
  },
];
export default {
  data() {
    return {
      columns,
      data,
      startdate: currentDate,
      startdate1: currentDate1,
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
  },
};
</script>
