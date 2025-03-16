<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <supportheader :title="title" />
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
                            :src="require('@/assets/img/profiles/' + record.img)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Customer }}
                          <span>{{ record.mail }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span :class="record.class">{{ record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                            class="feather feather-download"></i></a>
                        <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                            class="feather feather-eye"></i></a>
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-right">
                            <ul>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="feather feather-edit me-3"></i>Edit</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#delete_modal"><i class="far fa-trash-alt me-3"></i>Delete</a>
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

  <delete-modal :DeleteTitle="DeleteTitle" />
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
    title: "Customer",
    dataIndex: "Customer",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Customer.toLowerCase();
        b = b.Customer.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment ID",
    dataIndex: "PaymentID",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentID.toLowerCase();
        b = b.PaymentID.toLowerCase();
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
    title: "Payment Method",
    dataIndex: "PaymentMethod",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentMethod.toLowerCase();
        b = b.PaymentMethod.toLowerCase();
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
    key: "action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    img: "avatar-14.jpg",
    mail: "john@example.com",
    Customer: "John Smith",
    PaymentID: "#25689825",
    Amount: "$1,54,220",
    Date: "19 Dec 2023, 06:12 PM",
    PaymentMethod: "Cash",
    Status: "Success",
    class: "badge bg-success-light text-success-light",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    mail: "johnny@example.com",
    Customer: "Johnny",
    PaymentID: "#25689826",
    Amount: "$1,222",
    Date: "20 Nov 2023, 04:12 PM",
    PaymentMethod: "Cheque",
    Status: "Processing",
    class: "badge bg-warning-light text-warning-light",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    mail: "robert@example.com",
    Customer: "Robert",
    PaymentID: "#25689827",
    Amount: "$2,2222",
    Date: "21 Oct 2023, 07:12 AM",
    PaymentMethod: "Cheque",
    Status: "Failed",
    class: "badge bg-danger-light",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    mail: "sharon@example.com",
    Customer: "Sharonda",
    PaymentID: "#25689828",
    Amount: "$5,222",
    Date: "19 Sep 2023, 11:12 AM",
    PaymentMethod: "Cash",
    Status: "Success",
    class: "badge bg-success-light text-success-light",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    mail: "randall@example.com",
    Customer: "Randall",
    PaymentID: "#25689829",
    Amount: "$8,54,220",
    Date: "13 Nov 2023, 01:12 PM",
    PaymentMethod: "Cheque",
    Status: "Processing",
    class: "badge bg-warning-light text-warning-light",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    mail: "pricilla@example.com",
    Customer: "Pricilla",
    PaymentID: "#25689830",
    Amount: "$3,54,220",
    Date: "19 Dec 2023, 06:12 PM",
    PaymentMethod: "Cheque",
    Status: "Failed",
    class: "badge bg-danger-light",
  },
];
export default {
  setup() {
    return {
      title: "Payments",
      title1: "Delete Payments",
      DeleteTitle: "Delete Payments",
      data,
      columns,
    };
  },
};
</script>
