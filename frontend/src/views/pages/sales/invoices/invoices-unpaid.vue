<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <invoices-header :title="title" />
      <searchfilter />
      <invoicecard />
      <invoicetab />
      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'InvoiceID'">
                      <label class="custom_check">
                        <input type="checkbox" name="invoice" />
                        <span class="checkmark"></span>
                      </label>
                      <router-link to="/invoices/invoice-details" class="invoice-link">{{
                        record.InvoiceID
                      }}</router-link></template>
                    <template v-else-if="column.key === 'id'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-sm me-2">
                          <img class="avatar-img rounded-circle" :src="require(`@/assets/img/profiles/${record.img}`)"
                            alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.InvoiceTo
                        }}<span>{{ record.email }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span class="badge bg-light-gray text-secondary">{{
                        record.Status
                      }}</span></template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="text-end">
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-end">
                            <router-link class="dropdown-item" to="/invoices/edit-invoice"><i
                                class="far fa-edit me-2"></i>Edit</router-link>
                            <router-link class="dropdown-item" to="/invoices/invoice-details"><i
                                class="far fa-eye me-2"></i>View</router-link>
                            <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                              data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                            <a class="dropdown-item" href="javascript:;"><i class="feather feather-send me-2"></i>Send</a>
                            <a class="dropdown-item" href="javascript:;"><i
                                class="feather feather-download me-2"></i>Download</a>
                            <router-link class="dropdown-item" to="/sales/add-credit-notes"><i
                                class="feather feather-file-text me-2"></i>Convert to
                              Sales Return</router-link>
                            <a class="dropdown-item" href="javascript:;"><i class="feather feather-copy me-2"></i>Clone as
                              Invoice</a>
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
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
  <locationmodal :Delete="Delete" />
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
    title: "Invoice To",
    dataIndex: "InvoiceTo",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.InvoiceTo.toLowerCase();
        b = b.InvoiceTo.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Total",
    dataIndex: "Total",
    sorter: {
      compare: (a, b) => {
        a = a.Total.toLowerCase();
        b = b.Total.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Paid",
    dataIndex: "Paid",
    sorter: {
      compare: (a, b) => {
        a = a.Paid.toLowerCase();
        b = b.Paid.toLowerCase();
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
    title: "DueDate",
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
    class: "text-end",
    sorter: true,
  },
];
const data = [
  {
    InvoiceID: "#4991",
    Category: "Software",
    CreatedOn: "12 May 2023",
    img: "avatar-18.jpg",
    email: "+1 559-741-9672",
    InvoiceTo: "Pricilla",
    Total: "$5,54,220",
    Paid: "$3,50,000",
    PaymentMode: "Cheque",
    Balance: "$4,220",
    DueDate: "18 May 2023",
    Status: "Unpaid",
  },
];
export default {
  setup() {
    return {
      title: "Invoices Unpaid",
      Delete: "Delete Invoice",
      data,
      columns,
    };
  },
};
</script>
