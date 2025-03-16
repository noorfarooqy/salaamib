<template>
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
              data-bs-original-title="filter"
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
              data-bs-original-title="setting"
              ><span><i class="feather feather-settings"></i></span>
            </a>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              data-bs-original-title="grid-view"
              ><span><i class="feather feather-grid"></i></span>
            </a>
          </li>
          <li>
            <a
              class="active btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              data-bs-original-title="list-view"
              ><span><i class="feather feather-list"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
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

          <!-- Invoice Number -->
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
                  Invoice Number
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
                <div id="checkBoxes3">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 4905681
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 4905682
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 4905683
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> 4905684
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Two">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> 4905685
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> 4905686
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> 4905687
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
          <!-- /Invoice Number -->

          <!-- Payment Method -->
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
                  Payment Method
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
                <div id="checkBoxes4">
                  <div class="selectBox-cont">
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span>Cheque
                    </label>
                    <label class="custom_check w-100 mb-0">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Cash
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Payment Method -->

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
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
  },
  data() {
    return {};
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
