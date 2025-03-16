<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Vendor Ledger</h5>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <a class="btn btn-primary" href="#" data-bs-toggle="modal" data-bs-target="#add_ledger"><i
                    class="fa fa-plus-circle me-2" aria-hidden="true"></i>Create
                  Ledger</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- /Page Header -->

      <div class="card p-4 ledger-list">
        <div class="d-flex align-items-center justify-content-between">
          <div class="ledger-info mb-4">
            <div class="d-flex align-items-center">
              <router-link to="/profile" class="avatar me-2"><img class="avatar-img rounded-circle"
                  src="@/assets/img/profiles/avatar-14.jpg" alt="User Image" /></router-link>
              <h2>
                <router-link to="/profile">John Smith<a href="mailto:johnsmith@example.com"
                    class="d-block mail-to">johnsmith@example.com</a></router-link>
              </h2>
            </div>
          </div>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <div class="closing-balance">
                  <span class="d-flex align-items-center"><i class="fa fa-refresh me-2 text-danger-light"></i>Closing
                    Balance
                    : $400</span>
                </div>
              </li>
              <li>
                <div class="dropdown dropdown-action" data-bs-toggle="tooltip" data-bs-placement="top" title="Download">
                  <a href="#" class="btn-filters" data-bs-toggle="dropdown" aria-expanded="false"><span><i
                        class="feather feather-download"></i></span></a>
                  <div class="dropdown-menu dropdown-menu-end">
                    <ul class="d-block">
                      <li>
                        <a class="d-flex align-items-center download-item" href="javascript:void(0);" download><i
                            class="far fa-file-pdf me-2"></i>PDF</a>
                      </li>
                      <li>
                        <a class="d-flex align-items-center download-item" href="javascript:void(0);" download><i
                            class="far fa-file-text me-2"></i>CVS</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </li>
              <li>
                <a class="btn-filters" href="javascript:void(0);" data-bs-toggle="tooltip" data-bs-placement="bottom"
                  title="Print"><span><i class="feather feather-printer"></i></span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <!-- Table -->
        <div class="row">
          <div class="col-sm-12">
            <div class="card-table">
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-stripped table-hover">
                    <thead class="thead-light">
                      <tr>
                        <th>Name</th>
                        <th>Reference #</th>
                        <th>Created</th>
                        <th>Mode</th>
                        <th>Amount</th>
                        <th>Closing Balance</th>
                        <th class="no-sort">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>
                          <h2 class="ledger">PAYOUT -2 <span>Payment Out</span></h2>
                        </td>
                        <td>#25689825</td>
                        <td>16 Aug 2023, 06:12 PM</td>
                        <td><span class="badge bg-success-light">Cash</span></td>
                        <td><span class="text-danger-light">-$100</span></td>
                        <td><span>$400</span></td>
                        <td class="text-start">
                          <div class="dropdown dropdown-action">
                            <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                                class="fas fa-ellipsis-v"></i></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#edit_ledger"><i class="far fa-edit me-2"></i>Edit</a>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <h2 class="ledger">PAYIN -2<span>Payment In</span></h2>
                        </td>
                        <td>#25689826</td>
                        <td>14 Aug 2023, 04:07 PM</td>
                        <td><span class="badge bg-success-light">Cash</span></td>
                        <td><span class="text-success-light">+$200</span></td>
                        <td><span>$500</span></td>
                        <td class="text-start">
                          <div class="dropdown dropdown-action">
                            <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                                class="fas fa-ellipsis-v"></i></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#edit_ledger"><i class="far fa-edit me-2"></i>Edit</a>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <h2 class="ledger">PAYOUT -1<span>Payment Out</span></h2>
                        </td>
                        <td>#25689827</td>
                        <td>13 Aug 2023, 01:15 PM</td>
                        <td><span class="badge bg-success-light">Cash</span></td>
                        <td><span class="text-danger-light">-$200</span></td>
                        <td><span>$300</span></td>
                        <td class="text-start">
                          <div class="dropdown dropdown-action">
                            <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                                class="fas fa-ellipsis-v"></i></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#edit_ledger"><i class="far fa-edit me-2"></i>Edit</a>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <h2 class="ledger">PAYIN -1<span>Payment In</span></h2>
                        </td>
                        <td>#25689828</td>
                        <td>12 Aug 2023, 08:35 PM</td>
                        <td><span class="badge bg-success-light">Cash</span></td>
                        <td><span class="text-success-light">+$500</span></td>
                        <td><span>$500</span></td>
                        <td class="text-start">
                          <div class="dropdown dropdown-action">
                            <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                                class="fas fa-ellipsis-v"></i></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#edit_ledger"><i class="far fa-edit me-2"></i>Edit</a>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td colspan="4">
                          <p>Closing Balance as on 17/10/2023</p>
                          <span>Payment In</span>
                        </td>
                        <td><span class="text-success fw-600">$3000.15</span></td>
                        <td colspan="2">
                          <span class="text-primary fw-600">$500.24</span>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div class="mt-4 float-end">
                    <button type="button" class="btn btn-success me-2">
                      <i class="fa-solid fa-arrow-down me-2"></i>Credit
                    </button>
                    <button type="submit" class="btn btn-danger">
                      <i class="fa-solid fa-arrow-up me-2"></i>Debit
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Table -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
  <ledger-modal></ledger-modal>
</template>

<script>
const columns = [
  {
    title: "Name",
    dataIndex: "Name",
    key: "Name",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Reference",
    dataIndex: "Reference",
    sorter: {
      compare: (a, b) => {
        a = a.Reference.toLowerCase();
        b = b.Reference.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created",
    dataIndex: "Created",
    sorter: {
      compare: (a, b) => {
        a = a.Created.toLowerCase();
        b = b.Created.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Mode",
    dataIndex: "Mode",
    key: "Mode",
    sorter: {
      compare: (a, b) => {
        a = a.Mode.toLowerCase();
        b = b.Mode.toLowerCase();
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
    Image: "avatar-14.jpg",
    Name: "John Smith",
    Number: "+1 843-443-3282",
    Reference: "#25689825",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-success-light",
    Mode: "Credit",
  },
  {
    Image: "avatar-15.jpg",
    Name: "Johnny",
    Number: "+1 917-409-0861",
    Reference: "#25689826",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-danger-light",
    Mode: "Debit",
  },
  {
    Image: "avatar-16.jpg",
    Name: "Robert",
    Number: "+1 956-623-2880",
    Reference: "#25689827",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-success-light",
    Mode: "Credit",
  },
  {
    Image: "avatar-17.jpg",
    Name: "Sharonda",
    Number: "+1 956-623-2881",
    Reference: "#25689828",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-success-light",
    Mode: "Debit",
  },
  {
    Image: "avatar-18.jpg",
    Name: "Randall",
    Number: " +1 956-623-2882",
    Reference: "#25689829",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-danger-light",
    Mode: "Credit",
  },
  {
    Image: "avatar-19.jpg",
    Name: "Pricilla",
    Number: "+1 956-623-2883",
    Reference: "#25689830",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "text-success-light",
    Mode: "Debit",
  },
];

import { ref } from "vue";
const currentDate = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
      columns,
      data,
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
  },
};
</script>
