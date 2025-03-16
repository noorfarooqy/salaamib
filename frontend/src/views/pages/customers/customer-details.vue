<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Customer Details</h5>
        </div>
      </div>
      <div class="card customer-details-group">
        <div class="card-body">
          <div class="row align-items-center">
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-img d-inline-flex">
                    <img class="rounded-circle" src="@/assets/img/profiles/avatar-14.jpg" alt="" />
                  </span>
                  <div class="customer-details-cont">
                    <h6>John Smith</h6>
                    <p>Cl-12345</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-mail"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Email Address</h6>
                    <p>john@example.com</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-phone"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Phone Number</h6>
                    <p>585-785-4840</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-airplay"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Company Name</h6>
                    <p>Kanakku Corporation</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-globe"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Website</h6>
                    <p class="customer-mail">www.example.com</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-briefcase"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Company Address</h6>
                    <p>4712 Cherry Ridge Drive Rochester, NY 14620.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <!-- Inovices card -->
      <div class="row">
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-info-light">
                  <img src="@/assets/img/icons/receipt-item.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Total Invoice</div>
                  <div class="dash-counts">
                    <p>$298</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">02</span>
                </p>
                <p class="inovice-trending text-success-light">
                  02
                  <span class="ms-2"><i class="feather feather-trending-up"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-primary-light">
                  <img src="@/assets/img/icons/transaction-minus.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Outstanding</div>
                  <div class="dash-counts">
                    <p>$325,215</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">03</span>
                </p>
                <p class="inovice-trending text-success-light">
                  04
                  <span class="ms-2"><i class="feather feather-trending-up"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-warning-light">
                  <img src="@/assets/img/icons/archive-book.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Total Overdue</div>
                  <div class="dash-counts">
                    <p>$7825</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">01</span>
                </p>
                <p class="inovice-trending text-danger-light">
                  03
                  <span class="ms-2"><i class="feather feather-trending-down"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-primary-light">
                  <img src="@/assets/img/icons/clipboard-close.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Cancelled</div>
                  <div class="dash-counts">
                    <p>100</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">04</span>
                </p>
                <p class="inovice-trending text-danger-light">
                  05
                  <span class="ms-2"><i class="feather feather-trending-down"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-green-light">
                  <img src="@/assets/img/icons/message-edit.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Draft</div>
                  <div class="dash-counts">
                    <p>$125,586</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">06</span>
                </p>
                <p class="inovice-trending text-danger-light">
                  02
                  <span class="ms-2"><i class="feather feather-trending-down"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card inovices-card w-100">
            <div class="card-body">
              <div class="dash-widget-header">
                <span class="inovices-widget-icon bg-danger-light">
                  <img src="@/assets/img/icons/3d-rotate.svg" alt="" />
                </span>
                <div class="dash-count">
                  <div class="dash-title">Recurring</div>
                  <div class="dash-counts">
                    <p>$86,892</p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <p class="inovices-all">
                  No of Invoice <span class="rounded-circle bg-light-gray">03</span>
                </p>
                <p class="inovice-trending text-success-light">
                  02
                  <span class="ms-2"><i class="feather feather-trending-up"></i></span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Inovices card -->

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'InvoiceID'">
                      <label class="custom_check">
                        <input type="checkbox" name="invoice" />
                        <span class="checkmark"></span>
                      </label>
                      <router-link to="/invoices/invoice-details" class="invoice-link">{{
                        record.InvoiceID
                      }}</router-link>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <div>
                        <span v-if="record.Status === 'Paid'" class="badge bg-success-light text-success-light">{{
                          record.Status }}</span>
                        <span v-else-if="record.Status === 'Overdue'" class="badge bg-warning-light text-warning">{{
                          record.Status }}</span>
                        <span v-else-if="record.Status === 'Cancelled'" class="badge bg-danger-light">{{ record.Status
                        }}</span>
                        <span v-else-if="record.Status === 'Partially Paid'" class="badge bg-primary-light">{{
                          record.Status }}</span>

                        <span v-else-if="record.Status === 'Unpaid'" class="badge bg-light-gray text-secondary">{{
                          record.Status }}</span>
                        <span v-else-if="record.Status === 'Refunded'" class="badge bg-info-lights">{{ record.Status
                        }}</span>
                      </div>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="dropdown dropdown-action">
                        <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                            class="fas fa-ellipsis-v"></i></a>
                        <div class="dropdown-menu dropdown-menu-end customer-dropdown">
                          <ul>
                            <li>
                              <router-link class="dropdown-item" to="/customers/edit-customer"><i
                                  class="far fa-edit me-2"></i>Edit</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                            </li>
                            <li>
                              <router-link class="dropdown-item" to="customer-details"><i
                                  class="far fa-eye me-2"></i>View</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href=""><i class="feather feather-send me-2"></i>Send</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href=""><i class="feather feather-download me-2"></i>Download</a>
                            </li>
                            <li>
                              <router-link class="dropdown-item" to="/sales/add-credit-notes"><i
                                  class="feather feather-file-text me-2"></i>Convert
                                to Sales Return</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href=""><i class="feather feather-copy me-2"></i>Clone as
                                Invoice</a>
                            </li>
                          </ul>
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
      <!-- /Table -->
      <locationmodal :Delete="Delete" />
    </div>
  </div>
</template>

<script>
const columns = [
  {
    title: "Invoice ID",
    dataIndex: "InvoiceID",
    key: "InvoiceID",
    sorter: {
      compare: (a, b) => {
        a = a.InvoiceID.toLowerCase();
        b = b.InvoiceID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Category",
    dataIndex: "Category",
    sorter: {
      compare: (a, b) => {
        a = a.Category.toLowerCase();
        b = b.Category.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created On",
    dataIndex: "CreatedOn",
    sorter: {
      compare: (a, b) => {
        a = a.CreatedOn.toLowerCase();
        b = b.CreatedOn.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Total Amount",
    dataIndex: "TotalAmount",
    sorter: {
      compare: (a, b) => {
        a = a.TotalAmount.toLowerCase();
        b = b.TotalAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Paid Amount",
    dataIndex: "PaidAmount",
    sorter: {
      compare: (a, b) => {
        a = a.PaidAmount.toLowerCase();
        b = b.PaidAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Mode",
    dataIndex: "PaymentMode",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentMode.toLowerCase();
        b = b.PaymentMode.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Balance",
    dataIndex: "Balance",
    sorter: {
      compare: (a, b) => {
        a = a.Balance.toLowerCase();
        b = b.Balance.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Due Date",
    dataIndex: "DueDate",
    sorter: {
      compare: (a, b) => {
        a = a.DueDate.toLowerCase();
        b = b.DueDate.toLowerCase();
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
    title: "Action",
    key: "Action",
    sorter: true,
  },
];

const data = [
  {
    InvoiceID: "#4987",
    Category: "Food",
    Image: "avatar-14.jpg",
    Name: "John Smith",
    Email: "+1 843-443-3282",
    CreatedOn: "23 Mar 2023",
    TotalAmount: "$1,54,220",
    PaidAmount: "$1,50,000",
    PaymentMode: "Cash",
    Balance: "$2,54,00",
    DueDate: "25 Mar 2023",
    Class: "badge bg-success-light",
    Status: "Paid",
  },
  {
    InvoiceID: "#4988",
    Category: "Advertising",
    Image: "avatar-15.jpg",
    Name: "Johnny",
    Email: "+1 917-409-0861",
    CreatedOn: "16 Mar 2023",
    TotalAmount: "$3,54,220",
    PaidAmount: "$2,50,000",
    PaymentMode: "Cheque",
    Balance: "$4,220",
    DueDate: "16 Jan 2023",
    Class: "badge bg-success-light",
    Status: "Overdue",
  },
  {
    InvoiceID: "#4989",
    Image: "avatar-16.jpg",
    Name: "Robert",
    Email: "+1 956-623-2880",
    Category: "Marketing",
    CreatedOn: "25 Feb 2023",
    TotalAmount: "$1,54,220",
    PaidAmount: "$1,50,000",
    PaymentMode: "Cash",
    Balance: "$4,220",
    DueDate: "16 Jan 2023",
    Class: "badge bg-success-light",
    Status: "Cancelled",
  },
  {
    InvoiceID: "#4990",
    Category: "Repairs",
    Image: "avatar-17.jpg",
    Name: "Sharonda",
    Email: "+1 707-439-1732",
    CreatedOn: "25 Mar 2023",
    TotalAmount: "$1,54,220",
    PaidAmount: "$1,50,000",
    PaymentMode: "Cash",
    Balance: "$4,220",
    DueDate: "12 May 2023",
    Class: "badge bg-success-light",
    Status: "Partially Paid",
  },
  {
    InvoiceID: "#4991",
    Category: "Software",
    Image: "avatar-18.jpg",
    Name: "Pricilla",
    Email: "+1 559-741-9672",
    CreatedOn: "12 May 2023",
    TotalAmount: "$5,54,220",
    PaidAmount: "$3,50,000",
    PaymentMode: "Cheque",
    Balance: "$4,220",
    DueDate: "18 May 2023",
    Class: "badge bg-success-light",
    Status: "Unpaid",
  },
  {
    InvoiceID: "#4992",
    Category: "Stationary",
    Image: "avatar-19.jpg",
    Name: "Randall",
    Email: "+1 989-438-3131",
    CreatedOn: "16 Nov 2023",
    TotalAmount: "$5,54,220",
    PaidAmount: "$6,50,000",
    PaymentMode: "Cash",
    Balance: "$4,220",
    DueDate: "25 Feb 2023",
    Class: "badge bg-success-light",
    Status: "Refunded",
  },
];
export default {
  data() {
    return {
      title: "Customer Details",
      Delete: "Delete Customer Details",
      columns,
      data,
    };
  },
};
</script>
