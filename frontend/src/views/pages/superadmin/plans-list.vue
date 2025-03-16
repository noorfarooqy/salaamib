<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="subscription-plane-head">
        <ul>
          <li>
            <router-link to="/super-admin/packages" class="active"
              >Subscription Plans</router-link
            >
          </li>
          <li>
            <router-link to="/super-admin/subscription">Subscribers List</router-link>
          </li>
        </ul>
      </div>
      <!-- Page Header -->
      <packages-header></packages-header>
      <!-- /Page Header -->

      <div class="super-admin-list-head">
        <div class="row">
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card">
              <div class="card-body">
                <div class="grid-info-item total-plane">
                  <div class="grid-info">
                    <span>Total Plan</span>
                    <h4>07</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-package"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card">
              <div class="card-body">
                <div class="grid-info-item active-plane">
                  <div class="grid-info">
                    <span>Active Plans</span>
                    <h4>07</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-list"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card">
              <div class="card-body">
                <div class="grid-info-item inactive-plane">
                  <div class="grid-info">
                    <span>Inactive Plans</span>
                    <h4>0</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-pause-circle"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item total-type">
                  <div class="grid-info">
                    <span>No of Plan Types</span>
                    <h4>04</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-pocket"></i>
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
              <div class="table-responsive no-pagination">
                <div class="companies-table">
                  <a-table
                    class="table table-center table-hover datatable"
                    :columns="columns"
                    :data-source="data"
                  >
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'Status'">
                        <span
                          class="badge bg-success-light d-inline-flex align-items-center"
                          ><i class="feather feather-check me-1"></i
                          >{{ record.Status }}</span
                        >
                      </template>
                      <template v-if="column.key === 'Action'">
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
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#edit_package"
                                    ><i class="feather feather-edit me-2"></i>Edit</a
                                  >
                                </li>
                                <li class="delete-alt">
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"
                                    ><i class="feather feather-trash-2 me-2"></i>Delete</a
                                  >
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
  <packages-modal></packages-modal>
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
    title: "Plan Name",
    dataIndex: "PlanName",
    key: "PlanName",
    sorter: {
      compare: (a, b) => {
        a = a.PlanName.toLowerCase();
        b = b.PlanName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Plan Type",
    dataIndex: "PlanType",
    key: "PlanType",
    sorter: {
      compare: (a, b) => {
        a = a.PlanType.toLowerCase();
        b = b.PlanType.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Price",
    dataIndex: "Price",
    key: "Price",
    sorter: {
      compare: (a, b) => {
        a = a.Price.toLowerCase();
        b = b.Price.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Users",
    dataIndex: "Users",
    key: "Users",
    sorter: {
      compare: (a, b) => {
        a = a.Users.toLowerCase();
        b = b.Users.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Suppliers",
    dataIndex: "Suppliers",
    key: "Suppliers",
    sorter: {
      compare: (a, b) => {
        a = a.Suppliers.toLowerCase();
        b = b.Suppliers.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Products",
    dataIndex: "Products",
    sorter: {
      compare: (a, b) => {
        a = a.Products.toLowerCase();
        b = b.Products.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Invoice",
    dataIndex: "Invoice",
    sorter: {
      compare: (a, b) => {
        a = a.Invoice.toLowerCase();
        b = b.Invoice.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created Date",
    dataIndex: "CreatedDate",
    key: "CreatedDate",
    sorter: {
      compare: (a, b) => {
        a = a.CreatedDate.toLowerCase();
        b = b.CreatedDate.toLowerCase();
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
    id: "1",
    PlanName: "Free",
    PlanType: "Monthly",
    Price: "$00.00",
    Users: "2",
    Suppliers: "1",
    Products: "10",
    Invoice: "1",
    CreatedDate: "19 Jan 2024",
    Status: "Active",
  },
  {
    id: "2",
    PlanName: "Basic",
    PlanType: "Yearly",
    Price: "$19.99",
    Users: "5",
    Suppliers: "5",
    Products: "100",
    Invoice: "10",
    CreatedDate: "16 Jan 2024",
    Status: "Active",
  },
  {
    id: "3",
    PlanName: "Premium",
    PlanType: "Lifetime",
    Price: "$6549.99",
    Users: "50",
    Suppliers: "10",
    Products: "1000",
    Invoice: "1000",
    CreatedDate: "12 Jan 2024",
    Status: "Active",
  },
  {
    id: "4",
    PlanName: "Enterprise",
    PlanType: "Yearly",
    Price: "$99.99",
    Users: "1000",
    Suppliers: "Unlimited",
    Products: "Unlimited",
    Invoice: "Unlimited",
    CreatedDate: "9 Jan 2024",
    Status: "Active",
  },
  {
    id: "5",
    PlanName: "Advanced",
    PlanType: "Monthly",
    Price: "$499.99",
    Users: "Unlimited",
    Suppliers: "Unlimited",
    Products: "Unlimited",
    Invoice: "Unlimited",
    CreatedDate: "5 Jan 2024",
    Status: "Active",
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
