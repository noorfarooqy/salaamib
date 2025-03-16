<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <recurringheader :title="title" :path="path" :text="text" />

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'ID'">
                      <router-link to="credit-notes-details" class="invoice-link">{{
                        record.CreditNotesID
                      }}</router-link></template>
                    <template v-else-if="column.key === 'Customer'">
                      <h2 class="table-avatar d-flex align-center">
                        <router-link to="/profile" class="avatar avatar-sm me-2">
                          <img class="avatar-img rounded-circle" :src="require(`@/assets/img/profiles/${record.img}`)"
                            alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Customer
                        }}<span>{{ record.email }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span v-if="record.Status === 'Paid'" class="badge bg-success-light text-success-light">{{
                        record.Status }}</span>
                      <span v-else-if="record.Status === 'Pending'" class="badge bg-warning-light text-warning-light">{{
                        record.Status }}</span>
                      <span v-else-if="record.Status === 'Cancelled'" class="badge bg-danger-light">{{ record.Status
                      }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                            class="feather feather-download"></i></a>
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-right">
                            <ul>
                              <li>
                                <router-link class="dropdown-item" to="edit-credit-notes"><i
                                    class="far fa-edit me-2"></i>Edit</router-link>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                              </li>
                              <li>
                                <router-link class="dropdown-item" to="credit-notes-details"><i
                                    class="far fa-eye me-2"></i>View</router-link>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:;"><i
                                    class="feather feather-send me-2"></i>Send</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:;"><i
                                    class="feather feather-copy me-2"></i>Clone</a>
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
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
  <locationmodal :Delete="Delete" />
  <!-- /Main Wrapper -->
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    key: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Credit Notes ID",
    dataIndex: "CreditNotesID",
    key: "ID",
    sorter: {
      compare: (a, b) => {
        a = a.CreditNotesID.toLowerCase();
        b = b.CreditNotesID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "vendor",
    dataIndex: "Customer",
    key: "Customer",
    sorter: {
      compare: (a, b) => {
        a = a.Customer.toLowerCase();
        b = b.Customer.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
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
    NUM: "1",
    CreditNotesID: "#4987",
    img: "avatar-14.jpg",
    email: "+1 843-443-3282",
    Customer: "John Smith",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Paid",
  },
  {
    NUM: "2",
    CreditNotesID: "#4988",
    img: "avatar-15.jpg",
    email: "+1 917-409-0861",
    Customer: "Johnny",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Pending",
  },
  {
    NUM: "3",
    CreditNotesID: "#4989",
    img: "avatar-16.jpg",
    email: "+1 956-623-2880",
    Customer: "Robert",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Cancelled",
  },
  {
    NUM: "4",
    CreditNotesID: "#4990",
    img: "avatar-17.jpg",
    email: "+1 707-439-1732",
    Customer: "Sharonda",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Paid",
  },
  {
    NUM: "5",
    CreditNotesID: "#4991",
    img: "avatar-18.jpg",
    email: "+1 559-741-9672",
    Customer: "Pricilla",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Pending",
  },
  {
    NUM: "6",
    CreditNotesID: "#4992",
    img: "avatar-19.jpg",
    email: "+1 989-438-3131",
    Customer: "Randall",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "23 Mar 2023",
    Status: "Cancelled",
  },
];
export default {
  setup() {
    return {
      title: "Credit Notes",
      text: "Credit Notes",
      path: "add-credit-notes",
      Delete: "Delete Credit Notes",
      data,
      columns,
    };
  },
};
</script>
