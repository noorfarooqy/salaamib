<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <quotationsheader :title="title" :text="text" />

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
                        <router-link to="/profile">{{ record.Customer
                        }}<span>{{ record.num }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span class="badge bg-primary-light" v-if="record.Status === 'Sent'">{{ record.Status }}</span>
                      <span class="badge bg-success-light" v-else-if="record.Status === 'Accepted'">{{ record.Status
                      }}</span>
                      <span class="badge bg-danger-light" v-else-if="record.Status === 'Declined'">{{ record.Status
                      }}</span>
                      <span class="badge bg-light-gray text-secondary" v-else-if="record.Status === 'Expired'">{{
                        record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="dropdown dropdown-action">
                        <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                            class="fas fa-ellipsis-v"></i></a>
                        <div class="dropdown-menu dropdown-menu-right">
                          <ul>
                            <li>
                              <router-link class="dropdown-item" to="edit-quotations"><i
                                  class="far fa-edit me-2"></i>Edit</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);"><i
                                  class="feather feather-eye me-2"></i>View</a>
                            </li>
                            <li>
                              <router-link class="dropdown-item" to="/invoices/add-invoice"><i
                                  class="feather feather-file-text me-2"></i>Convert
                                to Invoice</router-link>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);"><i
                                  class="feather feather-arrow-right-circle me-2"></i>Mark as Sent</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);"><i
                                  class="feather feather-send me-2"></i>Send</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);"><i
                                  class="feather feather-copy me-2"></i>Clone as
                                Invoice</a>
                            </li>
                            <li>
                              <a class="dropdown-item" href="javascript:void(0);"><i
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
  <quotationmodel></quotationmodel>
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
    title: "Quotation ID",
    dataIndex: "QuotationID",
    sorter: {
      compare: (a, b) => {
        a = a.QuotationID.toLowerCase();
        b = b.QuotationID.toLowerCase();
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
    QuotationID: "#4905681",
    Customer: "John Smith",
    num: "+1 843-443-3282",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Sent",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    QuotationID: "#4905682",
    Customer: "Johnny",
    num: "+1 917-409-0861",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Accepted",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    QuotationID: "#4905683",
    Customer: "Robert",
    num: "+1 956-623-2880",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Declined",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    QuotationID: "#4905684",
    Customer: "Sharonda",
    num: "+1 707-439-1732",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Expired",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    QuotationID: "#4905685",
    Customer: "Randall",
    num: "+1 559-741-9672",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Sent",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    QuotationID: "#4905686",
    Customer: "Pricilla",
    num: "+1 989-438-3131",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Accepted",
  },
];
export default {
  data() {
    return {
      title: "Quotations",
      path: "add-quotations",
      text: "Create Quotation",
      DeleteTitle: "Delete Quotations",
      data,
      columns,
    };
  },
};
</script>
