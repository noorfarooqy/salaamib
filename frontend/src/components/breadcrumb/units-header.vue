<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>Units</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li >
            <div class="dropdown dropdown-action">
              <a
                href="javascript:;"
                class="btn-filters"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                ><span><i class="feather feather-download"></i></span
              ></a>
              <div class="dropdown-menu dropdown-menu-right">
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
            <a
              class="btn btn-primary"
              href="javascript:void(0);"
              data-bs-toggle="modal"
              data-bs-target="#add_unit"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Unit</a
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
          <!-- Product -->
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
                  Product Name
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
                          placeholder="Search Product"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lorem ipsum dolor sit
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lorem ipsum dolor sit
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lorem ipsum dolor sit
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lorem ipsum dolor sit
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Lorem ipsum dolor sit
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Lorem ipsum dolor sit
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Lorem ipsum dolor sit
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
          <!-- /Product -->

          <!-- Product Code -->
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
                  Product Code
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
                    <div class="form-custom">
                      <input
                        type="text"
                        class="form-control"
                        id="member_search2"
                        placeholder="Search Invoice"
                      />
                      <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                    </div>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> P125389
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> P125390
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> P125391
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> P125392
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Two">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> P125393
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> P125394
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> P125395
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
          <!-- /Product Code -->

          <!-- Unts -->
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
                  Units
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
                      <span class="checkmark"></span> Inches
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Pieces
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Hours
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Box
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Kilograms
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="bystatus" />
                      <span class="checkmark"></span> Meter
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Units -->

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
                <div id="checkBoxes4">
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
                      <span class="checkmark"></span> Marketing
                    </label>
                    <label class="custom_check w-100">
                      <input type="checkbox" name="category" />
                      <span class="checkmark"></span> Software
                    </label>
                    <!-- View All -->
                    <div class="view-content">
                      <div class="viewall-Three">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Repairs
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Stationary
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Designing
                        </label>
                      </div>
                      <div class="view-all">
                        <a href="javascript:void(0);" class="viewall-button-Three"
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
export default {
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
