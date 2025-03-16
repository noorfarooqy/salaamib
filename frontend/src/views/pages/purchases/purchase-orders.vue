<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <purchasesheader :title="title" :path="path" :text="text" />

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
                    <template v-else-if="column.key === 'Status'">
                      <span :class="record.class">{{ record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                            class="fas fa-ellipsis-v"></i></a>
                        <div class="dropdown-menu dropdown-menu-right credit-note-dropdown">
                          <ul>
                            <li>
                              <router-link class="dropdown-item" to="edit-purchases-order"><i
                                  class="far fa-edit me-2"></i>Edit</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                            </li>
                            <li>
                              <router-link class="dropdown-item" to="purchases-details"><i
                                  class="far fa-eye me-2"></i>View</router-link>
                            </li>
                            <li>
                              <router-link class="dropdown-item" to="add-purchase-return"><i
                                  class="feather feather-repeat me-2"></i>Convert To
                                Purchase</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:;"><i
                                  class="feather feather-send me-2"></i>Send</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:;"><i
                                  class="feather feather-copy me-2"></i>Clone</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:;"><i
                                  class="feather feather-download me-2"></i>Download</a>
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
    title: "Purchase ID",
    dataIndex: "PurchaseID",
    sorter: {
      compare: (a, b) => {
        a = a.PurchaseID.toLowerCase();
        b = b.PurchaseID.toLowerCase();
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
    title: "Date",
    dataIndex: "Date",
    sorter: {
      compare: (a, b) => {
        a = a.Date.toLowerCase();
        b = b.Date.toLowerCase();
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
    PurchaseID: "PO-100405361",
    Vendor: "John Smith",
    Amount: "$1,54,220",
    PaymentMode: "Cash",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Closed",
    class: "badge bg-success-light text-success-light",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    num: "+1 917-409-0861",
    PurchaseID: "PO-100405362",
    Vendor: "Johnny",
    Amount: "$2,54,220",
    PaymentMode: "Cheque",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Open",
    class: "badge bg-warning-light text-warning-light",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    num: "+1 956-623-2880",
    PurchaseID: "PO-100405363",
    Vendor: "Robert",
    Amount: "$1,84,220",
    PaymentMode: "Cash",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Closed",
    class: "badge bg-success-light text-success-light",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    num: "+1 707-439-1732",
    PurchaseID: "PO-100405364",
    Vendor: "Sharonda",
    Amount: "$6,54,220",
    PaymentMode: "Cheque",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Open",
    class: "badge bg-warning-light text-warning-light",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    num: "+1 559-741-9672",
    PurchaseID: "PO-100405365",
    Vendor: "Randall",
    Amount: "$3,54,220",
    PaymentMode: "Cash",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Closed",
    class: "badge bg-success-light text-success-light",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    num: "+1 989-438-3131",
    PurchaseID: "PO-100405366",
    Vendor: "Pricilla",
    Amount: "$1,54,220",
    PaymentMode: "Cheque",
    Date: "19 Dec 2023, 06:12 PM",
    Status: "Open",
    class: "badge bg-warning-light text-warning-light",
  },
];
export default {
  data() {
    return {
      title: "Purchase Orders",
      path: "add-purchases-order",
      text: "Add Purchase Orders",
      Delete: "Delete Purchases",
      data,
      columns,
    };
  },
};
</script>
