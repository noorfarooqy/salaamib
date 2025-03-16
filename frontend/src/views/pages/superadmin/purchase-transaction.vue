<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <superadminheader :title="title" />
      <!-- /Page Header -->

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <div class="purchase-table">
                  <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'Customer'">
                        <h2 class="table-avatar d-flex">
                          <router-link to="/profile">{{ record.Customer
                          }}<span>{{ record.Email }}</span></router-link>
                        </h2>
                      </template>
                      <template v-if="column.key === 'Status'">
                        <span :class="record.Class">{{ record.Status }}</span>
                      </template>
                      <template v-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <div class="dropdown dropdown-action">
                            <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                              aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                            <div class="dropdown-menu dropdown-menu-end">
                              <ul class="dropdown-ul">
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"><i
                                      class="fa-solid fa-eye me-2"></i>View</a>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"><i
                                      class="fa-solid fa-xmark me-2"></i>Cancel</a>
                                </li>
                                <li class="delete-alt">
                                  <div>
                                    <a class="dropdown-item" href="javascript:void(0);"><i
                                        class="fa-solid fa-edit me-2"></i>Subscription</a>
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
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>

<script>
const columns = [
  {
    title: "Bill #",
    dataIndex: "Bill",
    sorter: {
      compare: (a, b) => {
        a = a.Bill.toLowerCase();
        b = b.Bill.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Customer",
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
    title: "Mode",
    dataIndex: "Mode",
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
    id: "1",
    Bill: "INV-001",
    Customer: "Orn LLC",
    Email: "orn@example.com",
    CreatedOn: "15 Dec 2023, 04:35 PM",
    Amount: "$299.99",
    Status: "Paid",
    Class: "badge bg-success-light",
    Mode: "CASH",
  },
  {
    id: "2",
    Bill: "INV-005",
    Customer: "Accent Technology",
    Email: "accent@example.com",
    CreatedOn: "15 Dec 2023, 04:35 PM",
    Amount: "$299.99",
    Status: "Paid",
    Class: "badge bg-success-light",
    Mode: "UPI",
  },
  {
    id: "3",
    Bill: "INV-101",
    Customer: "Express Advertising",
    Email: "express@example.com",
    CreatedOn: "04 Dec 2023, 12:38 PM",
    Amount: "$299.99",
    Status: "Paid",
    Class: "badge bg-success-light",
    Mode: "UPI",
  },
  {
    id: "4",
    Bill: "INV-321",
    Customer: "Sumo Soft Limited",
    Email: "sumo@example.com",
    CreatedOn: "20 Nov 2023, 02:47 PM",
    Amount: "$299.99",
    Status: "Pending",
    Class: "badge bg-pending-light",
    Mode: "-",
  },
  {
    id: "5",
    Bill: "INV-333",
    Customer: "Repair Group Co",
    Email: "repair@example.com",
    CreatedOn: "15 Nov 2023, 10:42 AM",
    Amount: "$299.99",
    Status: "Pending",
    Class: "badge bg-pending-light",
    Mode: "-",
  },
  {
    id: "6",
    Bill: "INV-421",
    Customer: "Lexicon Technologies",
    Email: "lexicon@example.com",
    CreatedOn: "28 Nov 2023, 03:25 PM",
    Amount: "$299.99",
    Status: "Paid",
    Class: "badge bg-success-light",
    Mode: "CHEQUE",
  },
];
export default {
  data() {
    return {
      title: "Purchase Transaction",
      columns,
      data,
    };
  },
};
</script>
