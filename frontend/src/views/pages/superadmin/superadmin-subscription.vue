<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="subscription-plane-head">
        <ul>
          <li>
            <router-link to="/super-admin/packages">Subscription Plans</router-link>
          </li>
          <li>
            <router-link to="/super-admin/subscription" class="active"
              >Subscribers List</router-link
            >
          </li>
        </ul>
      </div>
      <!-- Page Header -->
     <subscription-header></subscription-header>
      <!-- /Page Header -->

      <div class="super-admin-list-head">
        <div class="row">
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item subscription-list total-transaction">
                  <div class="grid-head-icon">
                    <i class="feather feather-shield"></i>
                  </div>
                  <div class="grid-info">
                    <span>Total Transaction</span>
                    <h4>$6,565,60</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item subscription-list total-subscriber">
                  <div class="grid-head-icon">
                    <i class="feather feather-users"></i>
                  </div>
                  <div class="grid-info">
                    <span>Total Subscribers</span>
                    <h4>945</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item subscription-list active-subscriber">
                  <div class="grid-head-icon">
                    <i class="feather feather-user-check"></i>
                  </div>
                  <div class="grid-info">
                    <span>Active Subscriber</span>
                    <h4>944</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item subscription-list expired-subscriber">
                  <div class="grid-head-icon">
                    <i class="feather feather-user-x"></i>
                  </div>
                  <div class="grid-info">
                    <span>Expired</span>
                    <h4>1</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <div class="companies-table">
                  <a-table
                    class="table table-center table-hover datatable"
                    :columns="columns"
                    :data-source="data"
                  >
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'Subscriber'">
                        <h2 class="table-avatar">
                          <router-link
                            to="/profile"
                            class="company-avatar avatar-md me-2 companies company-icon"
                          >
                            <img
                              class="avatar-img rounded-circle company"
                              :src="require(`@/assets/img/companies/${record.Image}`)"
                              alt="Company Image"
                          /></router-link>
                          <a href="#">{{ record.Subscriber }}</a>
                        </h2>
                      </template>
                      <template v-else-if="column.key === 'Status'">
                        <div>
                          <span :class="record.Class"
                            ><i :class="record.Class1"></i>{{ record.Status }}</span
                          >
                        </div>
                      </template>
                      <template v-else-if="column.key === 'Invoice'">
                        <div>
                          <router-link
                            to="/super-admin/invoice-subscription"
                            class="invoice-detail"
                            ><i class="feather feather-file-text"></i
                          ></router-link>
                        </div>
                      </template>
                      <template v-else-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <div class="dropdown dropdown-action">
                            <a
                              href="#"
                              class="btn-action-icon"
                              data-bs-toggle="dropdown"
                              aria-expanded="false"
                              ><i class="fas fa-ellipsis-v"></i
                            ></a>
                            <div class="dropdown-menu dropdown-menu-end">
                              <ul class="dropdown-ul">
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-download me-2"></i
                                    >Download</a
                                  >
                                </li>
                                <li class="delete-alt">
                                  <div>
                                    <a
                                      class="dropdown-item"
                                      href="javascript:void(0);"
                                      data-bs-toggle="modal"
                                      data-bs-target="#delete_modal"
                                      ><i class="feather feather-trash-2 me-2"></i
                                      >Delete</a
                                    >
                                  </div>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </div>
                      </template>
                    </template>
                  </a-table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <subscription-model></subscription-model>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Subscriber",
    dataIndex: "Subscriber",
    key: "Subscriber",
    sorter: {
      compare: (a, b) => {
        a = a.Subscriber.toLowerCase();
        b = b.Subscriber.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Plan",
    dataIndex: "Plan",
    key: "Plan",
    sorter: {
      compare: (a, b) => {
        a = a.Plan.toLowerCase();
        b = b.Plan.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Billing Cycle",
    dataIndex: "BillingCycle",
    key: "BillingCycle",
    sorter: {
      compare: (a, b) => {
        a = a.BillingCycle.toLowerCase();
        b = b.BillingCycle.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Gateway",
    dataIndex: "PaymentGateway",
    key: "PaymentGateway",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentGateway.toLowerCase();
        b = b.PaymentGateway.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    key: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Registered On",
    dataIndex: "RegisteredOn",
    sorter: {
      compare: (a, b) => {
        a = a.RegisteredOn.toLowerCase();
        b = b.RegisteredOn.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Expiring On",
    dataIndex: "ExpiringOn",
    sorter: {
      compare: (a, b) => {
        a = a.ExpiringOn.toLowerCase();
        b = b.ExpiringOn.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Status",
    dataIndex: "Status",
    key: "Status",
    sorter: {
      compare: (a, b) => {
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Invoice",
    dataIndex: "Invoice",
    key: "Invoice",
    sorter: {
      compare: (a, b) => {
        a = a.Invoice.toLowerCase();
        b = b.Invoice.toLowerCase();
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
    id: "1",
    Subscriber: "Hermann Groups",
    Plan: "Advanced  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Paypal",
    Amount: "$19.99",
    RegisteredOn: "15 Jan 2024",
    ExpiringOn: "15 Feb 2024",
    Image: "company-01.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "2",
    Subscriber: "Skiles LLC",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "02 Mar 2024",
    Image: "company-02.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "3",
    Subscriber: "Kerluke Group",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Paypal",
    Amount: "$19.99",
    RegisteredOn: "18 Mar 2024",
    ExpiringOn: "18 Mar 2024",
    Image: "company-03.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "4",
    Subscriber: "Schowalter Group",
    Plan: "Premium (Yearly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$6549.99",
    RegisteredOn: "20 Apr 2024",
    ExpiringOn: "20 Apr 2024",
    Image: "company-04.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "5",
    Subscriber: "Accentric Global",
    Plan: "Advanced (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Debit Card",
    Amount: "$499.99",
    RegisteredOn: "12 May 2024",
    ExpiringOn: "12 May 2024",
    Image: "company-05.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "6",
    Subscriber: "Dexter Matrix",
    Plan: "Enterprise  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Paypal",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "Expired",
    Image: "company-06.svg",
    Status: "Unpaid",
    Class: "badge bg-danger-light d-inline-flex align-items-center",
    Class1: "feather feather-x me-1",
  },
  {
    id: "7",
    Subscriber: "Emporis Technologies",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "02 Mar 2024",
    Image: "company-07.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "8",
    Subscriber: "Beacon Softwares",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "02 Mar 2024",
    Image: "company-08.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "9",
    Subscriber: "Global tech",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "02 Mar 2024",
    Image: "company-09.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
  {
    id: "10",
    Subscriber: "High Tech Lead",
    Plan: "Basic  (Monthly)",
    BillingCycle: "30 Days",
    PaymentGateway: "Credit Card",
    Amount: "$499.99",
    RegisteredOn: "02 Feb 2024",
    ExpiringOn: "02 Mar 2024",
    Image: "company-10.svg",
    Status: "Paid",
    Class: "badge bg-success-light d-inline-flex align-items-center",
    Class1: "feather feather-check me-1",
  },
];
export default {
  data() {
    return {
      title: "Subscription",
      DeleteTitle: "Cancel Subscription",
      data,
      columns,
    };
  },
};
</script>
