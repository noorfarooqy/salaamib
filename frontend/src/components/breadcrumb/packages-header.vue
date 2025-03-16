<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>Plans List</h5>
      <div class="page-content">
        <div class="list-btn">
          <ul class="filter-list">
            <li>
              <router-link
                class="btn-filters"
                to="packages"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Grid-View"
                ><span><i class="feather feather-grid"></i></span
              ></router-link>
            </li>
            <li>
              <router-link
                class="btn-filters"
                to="/super-admin/plans-list"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="List-View"
                ><span><i class="feather feather-list"></i></span
              ></router-link>
            </li>
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
                @click="toggleFilter"
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
                  href="#"
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
                ><span class="me-2"><i class="feather feather-printer"></i></span>
                Print
              </a>
            </li>
            <li>
              <a
                class="btn btn-primary"
                href="#"
                data-bs-toggle="modal"
                data-bs-target="#add_newpackage"
                ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Plan</a
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Add Asset -->
  <div class="toggle-sidebar open-filter" v-if="isFilterOpen">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <a href="#" class="sidebar-closes" @click="closeSidebar"><i class="fa-regular fa-circle-xmark"></i></a>
      </div>
      <div class="sidebar-body">
        <form action="#" autocomplete="off">
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
                <div id="checkBoxes3">
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
                  Created Date
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