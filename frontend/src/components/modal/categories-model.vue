<template>
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
                      class="form-control datetimepicker"
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
                      class="form-control datetimepicker"
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
  <!-- modal -->
  <div class="modal modal-lg custom-modal fade" id="blog-categories" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Category</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="form-groups-item border-0 pb-0">
            <div class="row">
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Category Name<span class="text-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter Category Name"
                  />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Slug<span class="text-danger">*</span></label>
                  <input type="text" class="form-control" placeholder="Enter Slug" />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Description (Meta Tag)<span class="text-danger">*</span></label>
                  <input
                    type="text"
                    data-role="tagsinput"
                    class="input-tags form-control"
                    placeholder="Enter Tags"
                    name="services"
                  />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block">
                  <label>Keywords (Meta Tag)<span class="text-danger">*</span></label>
                  <input
                    type="text"
                    data-role="tagsinput"
                    class="input-tags form-control"
                    placeholder="Enter Tags"
                    name="services"
                  />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block">
                  <label>Order<span class="text-danger">*</span></label>
                  <input type="text" class="form-control" placeholder="Enter Order" />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block status-grid">
                  <label>Status</label>
                  <div class="status-toggle">
                    <input id="rating_9" class="check" type="checkbox" checked />
                    <label for="rating_9" class="checktoggle checkbox-bg"></label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add Category</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- modal -->
  <div
    class="modal custom-modal fade bank-details"
    id="edit-blog-categories"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header">
          <div class="form-header text-start mb-0">
            <h4 class="mb-0 text-dark fw-bold">Edit Category</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="bank-inner-details">
            <div class="row">
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Category Name<span class="text-danger">*</span></label>
                  <input type="text" class="form-control" value="Expenses" />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Slug<span class="text-danger">*</span></label>
                  <input type="text" class="form-control" value="Offer" />
                  <small class="form-text text-muted">
                    (If you leave it empty, it will be generated automatically.)</small
                  >
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Description (Meta Tag)<span class="text-danger">*</span></label>
                  <input
                    type="text"
                    data-role="tagsinput"
                    class="input-tags form-control"
                    placeholder="Enter Tags"
                    name="services"
                    value="Expenses "
                  />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Keywords (Meta Tag)<span class="text-danger">*</span></label>
                  <input
                    type="text"
                    data-role="tagsinput"
                    class="input-tags form-control"
                    placeholder="Enter Tags"
                    name="services"
                    value="Expenses "
                  />
                </div>
              </div>
              <div class="col-lg-4 col-md-12">
                <div class="input-block mb-3">
                  <label>Order<span class="text-danger">*</span></label>
                  <input type="text" class="form-control" value="3" />
                </div>
              </div>
              <div class="input-block mb-3">
                <label>Status</label>
                <div class="status-toggle">
                  <input id="rating_10" class="check" type="checkbox" checked />
                  <label for="rating_10" class="checktoggle checkbox-bg"></label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer blog-categories-btn">
          <div class="bank-details-btn">
            <a
              href="javascript:void(0);"
              data-bs-dismiss="modal"
              class="btn btn-primary me-2"
              >Add Category</a
            >
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
export default {
  data() {
    return {
      startdate: currentDate,
      startdate1: currentDate1,
      dateFormat: "dd-MM-yyyy", 
    };
  },
  mounted() {
    if (document.querySelectorAll(".popup-toggle").length > 0) {
      document.querySelectorAll(".popup-toggle").forEach(function (el) {
        el.addEventListener("click", function () {
          document.querySelector(".toggle-sidebar").classList.add("open-filter");
        });
      });

      document.querySelectorAll(".sidebar-closes").forEach(function (el) {
        el.addEventListener("click", function () {
          document.querySelector(".toggle-sidebar").classList.remove("open-filter");
        });
      });
    }
    if (document.querySelectorAll(".viewall-One").length > 0) {
      document.addEventListener("DOMContentLoaded", function () {
        var viewallOnes = document.querySelectorAll(".viewall-One");
        var viewallButton = document.querySelector(".viewall-button-One");

        viewallOnes.forEach(function (element) {
          element.style.display = "none";
        });

        viewallButton.addEventListener("click", function () {
          var buttonText = viewallButton.textContent;
          viewallOnes.forEach(function (element) {
            element.style.display = element.style.display === "none" ? "block" : "none";
          });

          viewallButton.textContent =
            buttonText === "Close All" ? "View All" : "Close All";
        });
      });
    }
    if (document.querySelectorAll(".viewall-Two").length > 0) {
      document.addEventListener("DOMContentLoaded", function () {
        var viewallOnes = document.querySelectorAll(".viewall-Two");
        var viewallButton = document.querySelector(".viewall-button-Two");

        viewallOnes.forEach(function (element) {
          element.style.display = "none";
        });

        viewallButton.addEventListener("click", function () {
          var buttonText = viewallButton.textContent;
          viewallOnes.forEach(function (element) {
            element.style.display = element.style.display === "none" ? "block" : "none";
          });

          viewallButton.textContent =
            buttonText === "Close All" ? "View All" : "Close All";
        });
      });
    }
    if (document.querySelectorAll(".viewall-Three").length > 0) {
      document.addEventListener("DOMContentLoaded", function () {
        var viewallOnes = document.querySelectorAll(".viewall-Three");
        var viewallButton = document.querySelector(".viewall-button-Three");

        viewallOnes.forEach(function (element) {
          element.style.display = "none";
        });

        viewallButton.addEventListener("click", function () {
          var buttonText = viewallButton.textContent;
          viewallOnes.forEach(function (element) {
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
