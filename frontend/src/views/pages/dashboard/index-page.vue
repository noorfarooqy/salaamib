<template>
  <div class="row">
    <div class="col-xl-3 col-sm-6 col-12">
      <div class="card">
        <div class="card-body">
          <div class="dash-widget-header">
            <span class="dash-widget-icon bg-1">
              <i class="fas fa-dollar-sign"></i>
            </span>
            <div class="dash-count">
              <div class="dash-title">Total Balance</div>
              <div class="dash-counts">
                <p>$24,642</p>
              </div>
            </div>
          </div>
          <div class="progress progress-sm mt-3">
            <div
              class="progress-bar bg-5"
              role="progressbar"
              style="width: 75%"
              aria-valuenow="75"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>
          <p class="text-muted mt-3 mb-0">
            <span class="text-success me-1"
              ><i class="fas fa-arrow-up me-1"></i>2.15%</span
            >
            since last month
          </p>
        </div>
      </div>
    </div>
    <div class="col-xl-3 col-sm-6 col-12">
      <div class="card">
        <div class="card-body">
          <div class="dash-widget-header">
            <span class="dash-widget-icon bg-2">
              <i class="fas fa-exchange-alt"></i>
            </span>
            <div class="dash-count">
              <div class="dash-title">Transactions</div>
              <div class="dash-counts">
                <p>1,245</p>
              </div>
            </div>
          </div>
          <div class="progress progress-sm mt-3">
            <div
              class="progress-bar bg-6"
              role="progressbar"
              style="width: 65%"
              aria-valuenow="75"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>
          <p class="text-muted mt-3 mb-0">
            <span class="text-success me-1"
              ><i class="fas fa-arrow-up me-1"></i>3.37%</span
            >
            since last month
          </p>
        </div>
      </div>
    </div>
    <div class="col-xl-3 col-sm-6 col-12">
      <div class="card">
        <div class="card-body">
          <div class="dash-widget-header">
            <span class="dash-widget-icon bg-3">
              <i class="fas fa-credit-card"></i>
            </span>
            <div class="dash-count">
              <div class="dash-title">Cards</div>
              <div class="dash-counts">
                <p>3</p>
              </div>
            </div>
          </div>
          <div class="progress progress-sm mt-3">
            <div
              class="progress-bar bg-7"
              role="progressbar"
              style="width: 85%"
              aria-valuenow="75"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>
          <p class="text-muted mt-3 mb-0">
            <span class="text-success me-1"
              ><i class="fas fa-arrow-up me-1"></i>1.77%</span
            >
            since last month
          </p>
        </div>
      </div>
    </div>
    <div class="col-xl-3 col-sm-6 col-12">
      <div class="card">
        <div class="card-body">
          <div class="dash-widget-header">
            <span class="dash-widget-icon bg-4">
              <i class="fas fa-piggy-bank"></i>
            </span>
            <div class="dash-count">
              <div class="dash-title">Savings</div>
              <div class="dash-counts">
                <p>$8,150</p>
              </div>
            </div>
          </div>
          <div class="progress progress-sm mt-3">
            <div
              class="progress-bar bg-8"
              role="progressbar"
              style="width: 45%"
              aria-valuenow="75"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>
          <p class="text-muted mt-3 mb-0">
            <span class="text-success me-1"
              ><i class="fas fa-arrow-up me-1"></i>4.68%</span
            >
            since last month
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-xl-7 d-flex">
      <div class="card flex-fill">
        <div class="card-header">
          <div class="d-flex justify-content-between align-items-center">
            <h5 class="card-title">Transaction Analytics</h5>

            <div class="dropdown">
              <button
                class="btn btn-white btn-sm dropdown-toggle"
                type="button"
                id="dropdownMenuButton"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Monthly
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Weekly</a>
                </li>
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Monthly</a>
                </li>
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Yearly</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="card-body">
          <div
            class="d-flex align-items-center justify-content-between flex-wrap flex-md-nowrap"
          >
            <div class="w-md-100 d-flex align-items-center mb-3 flex-wrap flex-md-nowrap">
              <div>
                <span>Total Deposits</span>
                <p class="h3 text-primary me-5">$12,500</p>
              </div>
              <div>
                <span>Total Withdrawals</span>
                <p class="h3 text-danger me-5">$5,800</p>
              </div>
              <div>
                <span>Net Flow</span>
                <p class="h3 text-success me-5">$6,700</p>
              </div>
              <div>
                <span>Pending</span>
                <p class="h3 text-warning me-5">$2,100</p>
              </div>
            </div>
          </div>

          <apexchart
            type="bar"
            height="350"
            :options="scolAreaChart.scol"
            :series="scolAreaChart.series"
          ></apexchart>
        </div>
      </div>
    </div>
    <div class="col-xl-5 d-flex">
      <div class="card flex-fill">
        <div class="card-header">
          <div class="d-flex justify-content-between align-items-center">
            <h5 class="card-title">Account Analytics</h5>

            <div class="dropdown">
              <button
                class="btn btn-white btn-sm dropdown-toggle"
                type="button"
                id="dropdownMenuButton1"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Monthly
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Weekly</a>
                </li>
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Monthly</a>
                </li>
                <li>
                  <a href="javascript:void(0);" class="dropdown-item">Yearly</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="card-body apexchart-index">
          <apexchart
            type="donut"
            height="350"
            :options="donutAreaCharts.donutchart"
            :series="donutAreaCharts.series"
          ></apexchart>

          <div class="text-center text-muted">
            <div class="row">
              <div class="col-4">
                <div class="mt-4">
                  <p class="mb-2 text-truncate">
                    <i class="fas fa-circle text-primary me-1"></i> Savings
                  </p>
                  <h5>$8,150</h5>
                </div>
              </div>
              <div class="col-4">
                <div class="mt-4">
                  <p class="mb-2 text-truncate">
                    <i class="fas fa-circle text-success me-1"></i> Checking
                  </p>
                  <h5>$16,492</h5>
                </div>
              </div>
              <div class="col-4">
                <div class="mt-4">
                  <p class="mb-2 text-truncate">
                    <i class="fas fa-circle text-danger me-1"></i> Investment
                  </p>
                  <h5>$4,250</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-md-6 col-sm-6">
      <div class="card mb-0">
        <div class="card-header">
          <div class="row align-center">
            <div class="col">
              <h5 class="card-title">Recent Transactions</h5>
            </div>
            <div class="col-auto">
              <router-link
                to="/transactions"
                class="btn-right btn btn-sm btn-outline-primary"
              >
                View All
              </router-link>
            </div>
          </div>
        </div>
        <div class="card-body">
          <div class="mb-3">
            <div class="progress progress-md rounded-pill mb-3">
              <div
                class="progress-bar bg-success"
                role="progressbar"
                style="width: 47%"
                aria-valuenow="47"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
              <div
                class="progress-bar bg-warning"
                role="progressbar"
                style="width: 28%"
                aria-valuenow="28"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
              <div
                class="progress-bar bg-danger"
                role="progressbar"
                style="width: 15%"
                aria-valuenow="15"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
              <div
                class="progress-bar bg-info"
                role="progressbar"
                style="width: 10%"
                aria-valuenow="10"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
            </div>
            <div class="row">
              <div class="col-auto">
                <i class="fas fa-circle text-success me-1"></i> Completed
              </div>
              <div class="col-auto">
                <i class="fas fa-circle text-warning me-1"></i> Pending
              </div>
              <div class="col-auto">
                <i class="fas fa-circle text-danger me-1"></i> Failed
              </div>
              <div class="col-auto">
                <i class="fas fa-circle text-info me-1"></i> Processing
              </div>
            </div>
          </div>

          <div class="table-responsive">
            <table class="table table-stripped table-hover">
              <thead class="thead-light">
                <tr>
                  <th>Description</th>
                  <th>Amount</th>
                  <th>Date</th>
                  <th>Status</th>
                  <th class="text-right">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <h2 class="table-avatar d-flex">
                      <span class="avatar avatar-sm me-2 avatar-img rounded-circle bg-success-light">
                        <i class="fas fa-arrow-down text-success"></i>
                      </span>
                      Salary Deposit
                    </h2>
                  </td>
                  <td>$3,500</td>
                  <td>23 Nov 2023</td>
                  <td><span class="badge bg-success-light">Completed</span></td>
                  <td class="text-right">
                    <div class="dropdown dropdown-action">
                      <a
                        href="javascript:;"
                        class="action-icon dropdown-toggle"
                        data-bs-toggle="dropdown"
                        aria-expanded="false"
                        ><i class="fas fa-ellipsis-h"></i
                      ></a>
                      <div class="dropdown-menu dropdown-menu-right">
                        <router-link class="dropdown-item" to="/transactions/details"
                          ><i class="far fa-eye me-2"></i>View Details</router-link
                        >
                        <a class="dropdown-item" href="javascript:void(0);"
                          ><i class="fas fa-print me-2"></i>Print Receipt</a
                        >
                        <a class="dropdown-item" href="javascript:void(0);"
                          ><i class="fas fa-download me-2"></i>Download PDF</a
                        >
                      </div>
                    </div>
                  </td>
                </tr>
                <!-- Similar structure for other transactions -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-sm-6">
      <div class="card mb-0">
        <div class="card-header">
          <div class="row align-center">
            <div class="col">
              <h5 class="card-title">Upcoming Payments</h5>
            </div>
            <div class="col-auto">
              <router-link
                to="/payments"
                class="btn-right btn btn-sm btn-outline-primary"
              >
                View All
              </router-link>
            </div>
          </div>
        </div>
        <div class="card-body">
          <div class="mb-3">
            <div class="progress progress-md rounded-pill mb-3">
              <div
                class="progress-bar bg-success"
                role="progressbar"
                style="width: 39%"
                aria-valuenow="39"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
              <div
                class="progress-bar bg-danger"
                role="progressbar"
                style="width: 35%"
                aria-valuenow="35"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
              <div
                class="progress-bar bg-warning"
                role="progressbar"
                style="width: 26%"
                aria-valuenow="26"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
            </div>
            <div class="row">
              <div class="col-auto">
                <i class="fas fa-circle text-success me-1"></i> Scheduled
              </div>
              <div class="col-auto">
                <i class="fas fa-circle text-warning me-1"></i> Pending
              </div>
              <div class="col-auto">
                <i class="fas fa-circle text-danger me-1"></i> Overdue
              </div>
            </div>
          </div>
          <div class="table-responsive">
            <table class="table table-hover">
              <thead class="thead-light">
                <tr>
                  <th>Description</th>
                  <th>Due Date</th>
                  <th>Amount</th>
                  <th>Status</th>
                  <th class="text-right">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <h2 class="table-avatar d-flex">
                      <span class="avatar avatar-sm me-2 avatar-img rounded-circle bg-warning-light">
                        <i class="fas fa-clock text-warning"></i>
                      </span>
                      Utility Bill Payment
                    </h2>
                  </td>
                  <td>5 Dec 2023</td>
                  <td>$175</td>
                  <td><span class="badge bg-warning-light text-warning">Pending</span></td>
                  <td class="text-right">
                    <div class="dropdown dropdown-action">
                      <a
                        href="javascript:;"
                        class="action-icon dropdown-toggle"
                        data-bs-toggle="dropdown"
                        aria-expanded="false"
                        ><i class="fas fa-ellipsis-h"></i
                      ></a>
                      <div class="dropdown-menu dropdown-menu-right">
                        <router-link class="dropdown-item" to="/payments/details"
                          ><i class="far fa-eye me-2"></i>View Details</router-link
                        >
                        <a class="dropdown-item" href="javascript:void(0);"
                          ><i class="fas fa-edit me-2"></i>Edit Payment</a
                        >
                        <a class="dropdown-item" href="javascript:void(0);"
                          ><i class="fas fa-times-circle me-2"></i>Cancel Payment</a
                        >
                      </div>
                    </div>
                  </td>
                </tr>
                <!-- Similar structure for other upcoming payments -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { scolAreaChart, donutAreaCharts } from "./data";
export default {
  data() {
    return {
      scolAreaChart: scolAreaChart,
      donutAreaCharts: donutAreaCharts,
    };
  },
};
</script>
