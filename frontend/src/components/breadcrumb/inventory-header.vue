<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>Inventory</h5>
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
            <div
              class="dropdown dropdown-action"
              data-bs-toggle="tooltip"
              data-bs-placement="top"
              data-bs-original-title="download"
            >
              <a
                href="javascript:;"
                class="btn-filters"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                ><span><i class="fether feather-download"></i></span
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
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              data-bs-original-title="print"
              ><span><i class="feather feather-printer"></i></span>
            </a>
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
                          <span class="checkmark"></span> Lenovo 3rd Generation
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Nike Jordan
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Apple Series 5 Watch
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Amazon Echo Dot
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Lobar Handy
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Woodcraft Sandal
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
                  Product Code
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
  <!-- /Add Asset -->
</template>
<script>
export default {
  data() {
    return {};
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
