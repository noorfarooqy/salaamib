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

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Customer</h3>
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
