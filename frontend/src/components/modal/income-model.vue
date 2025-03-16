<template>
  <!-- Add New Modal -->
  <div class="modal custom-modal fade" id="add_ledger" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Ledger</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="page-header add">
          <div class="content-page-header add">
            <div class="add-header">
              <h6>Test Company</h6>
              <p>You Pay $400</p>
            </div>
            <div class="list-btn">
              <ul class="filter-list">
                <li >
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
        <!-- Table -->
        <div class="modal-body add">
          <div class="addnew-modal">
            <div class="row">
              <div class="col-sm-12">
                <div class="card-table">
                  <div class="card-body">
                    <div class="table-responsive">
                      <div class="companies-table Ledger">
                        <table class="table table-center table-hover datatable">
                          <thead class="thead-light">
                            <tr>
                              <th>Id #</th>
                              <th>Date</th>
                              <th>Mode</th>
                              <th>Amount</th>
                              <th>Closing Balance</th>
                              <th class="no-sort">Action</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>
                                <h2 class="table-avatar d-flex">
                                  <a> PAYOUT -2<span>Payment Out</span></a>
                                </h2>
                              </td>
                              <td>16 Aug 2023</td>
                              <td><span class="badge bg-success-light">Cash</span></td>
                              <td><span class="text-danger-light">- $100</span></td>
                              <td>$400</td>
                              <td class="d-flex align-items-center">
                                <a class="btn-action-icon me-2" href="javascript:void(0);"
                                  ><i class="feather feather-edit"></i
                                ></a>
                                <a class="btn-action-icon" href="javascript:void(0);"
                                  ><i class="feather feather-trash-2"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <h2 class="table-avatar d-flex">
                                  <a> PAYIN -2<span>Payment In</span></a>
                                </h2>
                              </td>
                              <td>14 Aug 2023</td>
                              <td><span class="badge bg-success-light">Cash</span></td>
                              <td><span class="text-success-light">+ $200</span></td>
                              <td>$500</td>
                              <td class="d-flex align-items-center">
                                <a class="btn-action-icon me-2" href="javascript:void(0);"
                                  ><i class="feather feather-edit"></i
                                ></a>
                                <a class="btn-action-icon" href="javascript:void(0);"
                                  ><i class="feather feather-trash-2"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <h2 class="table-avatar d-flex">
                                  <a> PAYOUT -1<span>Payment Out</span></a>
                                </h2>
                              </td>
                              <td>13 Aug 2023</td>
                              <td><span class="badge bg-success-light">Cash</span></td>
                              <td><span class="text-danger-light">- $200</span></td>
                              <td>$300</td>
                              <td class="d-flex align-items-center">
                                <a class="btn-action-icon me-2" href="javascript:void(0);"
                                  ><i class="feather featherer feather-edit"></i
                                ></a>
                                <a class="btn-action-icon" href="javascript:void(0);"
                                  ><i class="feather featherer feather-trash-2"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <h2 class="table-avatar d-flex">
                                  <a>PAYIN -1<span>Payment In</span></a>
                                </h2>
                              </td>
                              <td>12 Aug 2023</td>
                              <td><span class="badge bg-success-light">Cash</span></td>
                              <td><span class="text-success-light">+$500</span></td>
                              <td>$500</td>
                              <td class="d-flex align-items-center">
                                <a class="btn-action-icon me-2" href="javascript:void(0);"
                                  ><i class="feather feather-edit"></i
                                ></a>
                                <a class="btn-action-icon" href="javascript:void(0);"
                                  ><i class="feather feather-trash-2"></i
                                ></a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Table -->

            <div class="modal-footer add">
              <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-success me-2"
                ><i class="fa-solid fa-arrow-down"></i>Credit</a
              >
              <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-danger"
                ><i class="fa-solid fa-arrow-up"></i>Add New</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

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
          <div class="accordion accordion-last" id="accordionMain1">
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
                  Company
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
                          placeholder="Search Customer"
                        />
                        <span><img src="@/assets/img/icons/search.svg" alt="img" /></span>
                      </div>
                      <div class="selectBox-cont">
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Orn LLC
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Accent Technology
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Express Advertising
                        </label>
                        <label class="custom_check w-100">
                          <input type="checkbox" name="username" />
                          <span class="checkmark"></span> Lexicon Technologies
                        </label>
                        <!-- View All -->
                        <div class="view-content">
                          <div class="viewall-One">
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Sumo Soft Limited
                            </label>
                            <label class="custom_check w-100">
                              <input type="checkbox" name="username" />
                              <span class="checkmark"></span> Repair Group Co
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
export default {
  data() {
    return {};
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
