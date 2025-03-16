<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>Companies</h5>
      <div class="page-content">
        <div class="list-btn">
          <ul class="filter-list">
            <li>
              <a
                class="btn-filters"
                href="javascript:void(0);"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Refresh"
                ><span><i class="feather feather-refresh-ccw"></i></span
              ></a>
            </li>
            <li>
              <a
                class="btn btn-filters w-auto popup-toggle"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Filter"
                @click="toggleFilter"
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
                  href="id"
                  class="btn btn-filters"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                  ><span class="me-2"><i class="feather feather-download"></i></span
                  >Export</a
                >
                <div class="dropdown-menu dropdown-menu-end">
                  <ul class="d-block">
                    <li>
                      <a
                        class="d-flex align-items-center download-item"
                        href="javascript:void(0);"
                        download
                        ><i class="far fa-file-pdf me-2"></i>Export as PDF</a
                      >
                    </li>
                    <li>
                      <a
                        class="d-flex align-items-center download-item"
                        href="javascript:void(0);"
                        download
                        ><i class="far fa-file-text me-2"></i>Export as Excel</a
                      >
                    </li>
                  </ul>
                </div>
              </div>
            </li>
            <li>
              <a
                class="btn btn-filters"
                href="javascript:void(0);"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Print"
                ><span class="me-2"><i class="feather feather-printer"></i></span> Print
              </a>
            </li>
            <li>
              <a
                class="btn btn-primary"
                href="id"
                data-bs-toggle="modal"
                data-bs-target="#add_companies"
                ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Company</a
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Header -->

  <!-- Add Asset -->
  <div class="toggle-sidebar open-filter" v-if="isFilterOpen">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="#" class="sidebar-closes" @click="closeSidebar"><i class="fa-regular fa-circle-xmark"></i></a>
      </div>
      <div class="sidebar-body">
        <form action="#" autocomplete="off">
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
                  Company Name
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
                          class="form-control member-search-dropdown"
                          id="member_search1"
                          placeholder="Search Company"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont search-dropdown-item">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Hermann Groups
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Skiles LLC
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Kerluke Group
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>Schowalter Group
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Accentric Global
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Dexter Matrix
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Emporis Technologies
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>High Tech Lead
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span> Beacon Softwares
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="bystatus" />
                          <span class="checkmark"></span>Global tech
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Customer -->

          <!-- By Plane -->
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
                  Plans
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
                      <span class="checkmark"></span> All Plans
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Advanced
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Basic
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Enterprise
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Premium
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Free
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Plane -->

          <!-- By Plane -->
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
                  Plans Type
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
                <div id="checkBoxes2">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> All Plan Type
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Monthly
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Weekly
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span>Lifetime
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /By Plane -->

          <!-- Select Date -->
          <div class="accordion accordion-last" id="accordionMain2">
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
                      class="form-control datetimepicker"
                      :editable="true"
                      :clearable="false"
                      placeholder="DD-MM-YYYY"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
                <div class="input-block mb-3">
                  <label class="form-control-label">To</label>
                  <div class="cal-icon">
                    <date-picker
                      v-model="startdateOne"
                      class="form-control datetimepicker"
                      :editable="true"
                      :clearable="false"
                      placeholder="DD-MM-YYYY"
                      :input-format="dateFormat"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Select Date -->

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
  data() {
    return {
      isFilterOpen: false,
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
    };
  },
  methods: {
    toggleFilter() {
      this.isFilterOpen = !this.isFilterOpen;
    },
    closeSidebar() {
      this.isFilterOpen = false;
    },
  },
};
</script>