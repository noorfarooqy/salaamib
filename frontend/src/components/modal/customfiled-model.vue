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
                      v-model="startdate"
                      type="email"
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
                      v-model="startdate1"
                      type="email"
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

  <!-- Add New Modal -->
  <div class="modal custom-modal fade" id="add_custom" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
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
        <div class="modal-body add">
          <div class="addnew-modal">
            <div class="row">
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Custom Fields For <span class="text-danger">*</span> </label>
                  <ul class="form-group">
                    <li>
                      <vue-select :options="Customplan" placeholder="Plan" />
                    </li>
                  </ul>
                </div>
              </div>

              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Label <span class="text-danger">*</span> </label>
                  <input type="text" class="form-control" placeholder="Enter Label" />
                </div>
              </div>
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Default Value</label>
                  <input type="text" class="form-control" placeholder="Enter Value" />
                </div>
              </div>
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Input Type <span class="text-danger">*</span> </label>
                  <ul class="form-group">
                    <li>
                      <vue-select :options="Customtext" placeholder="Text" />
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="input-block add mb-3 row">
            <div class="col-md-3">
              <div class="checkbox">
                <label class="mb-0 d-flex align-items-center">
                  <input type="checkbox" name="checkbox" /> Required
                </label>
              </div>
            </div>
            <div class="col-md-3">
              <div class="checkbox">
                <label class="mb-0 d-flex align-items-center">
                  <input type="checkbox" name="checkbox" />Disable
                </label>
              </div>
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-md-12 d-flex align-items-center justify-content-between">
              <div class="two-factor content p-0">
                <h6>Status</h6>
              </div>
              <div class="addnew-checkbox">
                <div class="status-toggle">
                  <input id="rating_1" class="check" type="checkbox" checked="" />
                  <label for="rating_1" class="checktoggle checkbox-bg factor"
                    >checkbox</label
                  >
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer add">
            <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
              >Cancel</a
            >
            <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
              >Save Changes</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Modal -->
  <div class="modal custom-modal fade" id="edit" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Custom Fields</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body add">
          <div class="addnew-modal">
            <div class="row">
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Custom Fields For <span class="text-danger">*</span> </label>
                  <ul class="form-group">
                    <li>
                      <vue-select :options="Customplanone" placeholder="Plan" />
                    </li>
                  </ul>
                </div>
              </div>

              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Label <span class="text-danger">*</span> </label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Label"
                    value="Email"
                  />
                </div>
              </div>
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Default Value</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Value"
                    value="Enter Email"
                  />
                </div>
              </div>
              <div class="col-lg-12 col-sm-12">
                <div class="input-block mb-3">
                  <label>Input Type <span class="text-danger">*</span> </label>
                  <ul class="form-group">
                    <li>
                      <vue-select :options="Customtextone" placeholder="Plan" />
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="input-block add mb-3 row">
            <div class="col-md-3">
              <div class="checkbox">
                <label class="mb-0 d-flex align-items-center">
                  <input type="checkbox" name="checkbox" checked /> Required
                </label>
              </div>
            </div>
            <div class="col-md-3">
              <div class="checkbox">
                <label class="mb-0 d-flex align-items-center">
                  <input type="checkbox" name="checkbox" />Disable
                </label>
              </div>
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-md-12 d-flex align-items-center justify-content-between">
              <div class="two-factor content p-0">
                <h6>Status</h6>
              </div>
              <div class="addnew-checkbox">
                <div class="status-toggle">
                  <input id="rating_1" class="check" type="checkbox" checked="" />
                  <label for="rating_1" class="checktoggle checkbox-bg factor"
                    >checkbox</label
                  >
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer add">
            <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
              >Cancel</a
            >
            <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
              >Save Changes</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Modal -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDate1 = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      startdate1: currentDate1,
      dateFormat: "dd-MM-yyyy",  
      Customplan: ["Plan", "Companies", "Ledger", "Package"],
      Customtext: ["Text", "Text Area", "Select", "Phone Number", "Email"],
      Customplanone: ["Plan", "Companies", "Ledger", "Package"],
      Customtextone: ["Text", "Text Area", "Select", "Phone Number", "Email"],
    };
  },
};
</script>
