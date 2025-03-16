<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <debitnotesheader :title="title" :path="path" :text="text" />

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

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Vendor }}<span>{{ record.num }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'debit'">
                      <router-link to="/invoices/invoice-details" class="invoice-link">{{
                        record.DebitNotesID
                      }}</router-link>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span class="badge bg-success-light text-success-light" v-if="record.Status === 'Paid'">{{
                        record.Status }}</span>
                      <span class="badge bg-warning-light text-warning-light" v-else-if="record.Status === 'Pending'">{{
                        record.Status }}</span>
                      <span class="badge bg-danger-light" v-else-if="record.Status === 'Cancelled'">{{ record.Status
                      }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                            class="feather feather-download"></i></a>
                        <div class="dropdown dropdown-action">
                          <a href="#" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                              class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-right">
                            <ul>
                              <li>
                                <router-link class="dropdown-item" to="edit-purchase-return"><i
                                    class="far fa-edit me-2"></i>Edit</router-link>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href=""><i class="far fa-eye me-2"></i>View</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href=""><i class="feather feather-send me-2"></i>Send</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href=""><i class="feather feather-copy me-2"></i>Clone</a>
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
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Debit Notes ID",
    dataIndex: "DebitNotesID",
    key: "debit",
    sorter: {
      compare: (a, b) => {
        a = a.DebitNotesID.toLowerCase();
        b = b.DebitNotesID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Vendor",
    dataIndex: "Vendor",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Vendor.toLowerCase();
        b = b.Vendor.toLowerCase();
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
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    img: "avatar-14.jpg",
    num: "+1 843-443-3282",
    DebitNotesID: "#4905681",
    Vendor: "John Smith",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Paid",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    num: "+1 917-409-0861",
    DebitNotesID: "#4905682",
    Vendor: "Rober",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "15 Dec 2023, 04:35 PM",
    Status: "Pending",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    num: "+1 956-623-2880",
    DebitNotesID: "#4905683",
    Vendor: "Johnny",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "04 Dec 2023, 12:38 PM",
    Status: "Cancelled",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    num: "+1 707-439-1732",
    DebitNotesID: "#4905684",
    Vendor: "Randall",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "28 Nov 2023, 03:25 PM",
    Status: "Paid",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    num: "+1 559-741-9672",
    DebitNotesID: "#4905685",
    Vendor: "Russell Copeland",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "20 Nov 2023, 02:47 PM",
    Status: "Pending",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    num: "+1 989-438-3131",
    DebitNotesID: "#4905686",
    Vendor: "Barbara Moore",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    CreatedOn: "15 Nov 2023, 10:42 AM",
    Status: "Cancelled",
  },
];
export default {
  data() {
    return {
      title: "Purchase Returns / Debit Notes",
      path: "add-purchase-return",
      text: "Add Purchase Returns / Debit Notes",
      Delete: "Delete Debit Notes",
      data,
      columns,
    };
  },
};
</script>
