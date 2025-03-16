<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <companies-header></companies-header>
      <!-- /Page Header -->

      <div class="super-admin-list-head">
        <div class="row">
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item total-items">
                  <div class="grid-info">
                    <span>Total Companies</span>
                    <h4>987</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-life-buoy"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item active-items">
                  <div class="grid-info">
                    <span>Active Companies</span>
                    <h4>154</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-check-square"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item inactive-items">
                  <div class="grid-info">
                    <span>Inactive Company</span>
                    <h4>2</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-x-circle"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 d-flex">
            <div class="card w-100">
              <div class="card-body">
                <div class="grid-info-item location-info">
                  <div class="grid-info">
                    <span>Company Locations</span>
                    <h4>200</h4>
                  </div>
                  <div class="grid-head-icon">
                    <i class="feather feather-map-pin"></i>
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
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <div class="companies-table">
                  <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'Name'">
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
                          <router-link to="/super-admin/companies">{{record.Name}}</router-link>
                        </h2>
                      </template>
                      <template v-if="column.key === 'Change_Plan'">
                          <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#change_pane"
                            ><span class="badge bg-purple">{{record.Change_Plan}}</span></a
                          >
                      </template>
                      <template v-if="column.key === 'Status'">
                          <span :class="record.Status_Class"
                            ><i :class="record.Icon"></i>{{record.Status}}</span
                          >
                      </template>
                      <template v-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <div class="dropdown dropdown-action">
                            <a
                              href="id"
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
                                    data-bs-target="#view_companies"
                                    ><i class="far fa-eye me-2"></i>View Company</a
                                  >
                                </li>
                                <li>
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#edit_companies"
                                    ><i class="feather feather-edit me-2"></i>Edit</a
                                  >
                                </li>
                                <li class="delete-alt">
                                  <div>
                                    <a
                                      class="dropdown-item"
                                      href="javascript:void(0);"
                                      data-bs-toggle="modal"
                                      data-bs-target="#delete_modal"
                                      ><i class="feather feather-trash-2 me-2"></i>Delete</a
                                    >
                                  </div>
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-user-x me-2"></i>Cancel Plan</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-shuffle me-2"></i>Subscription Log</a
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

  <companies-model></companies-model>
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
    title: "Name",
    dataIndex: "Name",
    key: "Name",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Email",
    dataIndex: "Email",
    sorter: {
      compare: (a, b) => {
        a = a.Email.toLowerCase();
        b = b.Email.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Account URL",
    dataIndex: "Account_URL",
    sorter: {
      compare: (a, b) => {
        a = a.Account_URL.toLowerCase();
        b = b.Account_URL.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Plan",
    dataIndex: "Plan",
    sorter: {
      compare: (a, b) => {
        a = a.Plan.toLowerCase();
        b = b.Plan.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Change Plan",
    dataIndex: "Change_Plan",
    key: "Change_Plan",
    sorter: {
      compare: (a, b) => {
        a = a.Change_Plan.toLowerCase();
        b = b.Change_Plan.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created Date",
    dataIndex: "Created_Date",
    sorter: {
      compare: (a, b) => {
        a = a.Created_Date.toLowerCase();
        b = b.Created_Date.toLowerCase();
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
   "id": "1",
   "Image": "company-01.svg",
   "Name": "Hermann Groups",
   "Email": "info@example.com",
   "Account_URL": "hru.example.com",
   "Plan": "Advanced (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "19 Jan 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "2",
   "Image": "company-02.svg",
   "Name": "Skiles LLC",
   "Email": "sales@example.com",
   "Account_URL": "sk.example.com",
   "Plan": "Basic (Yearly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Jan 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "3",
   "Image": "company-03.svg",
   "Name": "Kerluke Group",
   "Email": "info@example.com",
   "Account_URL": "kerluke.example.com",
   "Plan": "Enterprise (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "04 Jan 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "4",
   "Image": "company-04.svg",
   "Name": "Schowalter Group",
   "Email": "user233@example.com",
   "Account_URL": "schowalter.example.com",
   "Plan": "Advanced (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "28 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "5",
   "Image": "company-05.svg",
   "Name": "Accentric Global",
   "Email": "accounts@example.com",
   "Account_URL": "accentric.example.com",
   "Plan": "Advanced (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "20 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "6",
   "Image": "company-06.svg",
   "Name": "Dexter Matrix",
   "Email": "sales@example.com",
   "Account_URL": "dexter.example.com",
   "Plan": "Premium (Yearly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "7",
   "Image": "company-07.svg",
   "Name": "Emporis Technologies",
   "Email": "info@example.com",
   "Account_URL": "emporis.example.com",
   "Plan": "Free (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "8",
   "Image": "company-08.svg",
   "Name": "Beacon Softwares",
   "Email": "business@example.com",
   "Account_URL": "beacon.example.com",
   "Plan": "Enterprise (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "9",
   "Image": "company-09.svg",
   "Name": "Global tech",
   "Email": "user234@example.com",
   "Account_URL": "global.example.com",
   "Plan": "Free (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Feb 2024",
   "Icon": "feather feather-check me-1",
   "Status": "Active",
   "Status_Class": "badge bg-success-light d-inline-flex align-items-center"
 },
 {
   "id": "10",
   "Image": "company-10.svg",
   "Name": "High Tech Lead",
   "Email": "accounts@example.com",
   "Account_URL": "high.example.com",
   "Plan": "Enterprise (Monthly)",
   "Change_Plan": "Change",
   "Created_Date": "15 Feb 2024",
   "Icon": "feather feather-x me-1",
   "Status": "Inactive",
   "Status_Class": "badge bg-danger-light d-inline-flex align-items-center"
 }
]
export default {
  data() {
    return {
      title: "Companies",
      DeleteTitle: "Delete Companies",
      data,
      columns,
    };
  },
};
</script>
