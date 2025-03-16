<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- /Page Header -->
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar></settingsidebar>
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="page-header">
            <div class="content-page-header">
              <h5>Custom Fields</h5>
              <div class="page-content">
                <div class="list-btn">
                  <ul class="filter-list">
                    <li>
                      <a class="btn btn-filters w-auto popup-toggle" data-bs-toggle="tooltip" data-bs-placement="bottom"
                        title="Filter"><span class="me-2"><img src="@/assets/img/icons/filter-icon.svg"
                            alt="filter" /></span>Filter
                      </a>
                    </li>
                    <li>
                      <a class="btn btn-primary" href="javascript:void(0);" data-bs-toggle="modal"
                        data-bs-target="#add_custom"><i class="fa-solid fa-plus" aria-hidden="true"></i>Add New</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <!-- /Page Header -->

          <!-- Table -->
          <div class="row">
            <div class="col-sm-12">
              <div class="card-table">
                <div class="card-body">
                  <div class="table-responsive">
                    <div class="companies-table filed">
                      <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                        <template #bodyCell="{ column }">
                          <template v-if="column.key === 'Action'">
                            <div class="d-flex align-items-center">
                              <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                                data-bs-target="#edit"><i class="feather feather-edit"></i></a>
                              <a class="btn-action-icon" href="javascript:void(0);" data-bs-toggle="modal"
                                data-bs-target="#delete_modal"><i class="feather feather-trash-2"></i></a>
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

      <customfiledmodel></customfiledmodel>
    </div>
  </div>
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
    title: "Modules",
    dataIndex: "Modules",
    sorter: {
      compare: (a, b) => {
        a = a.Modules.toLowerCase();
        b = b.Modules.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Label",
    dataIndex: "Label",
    sorter: {
      compare: (a, b) => {
        a = a.Label.toLowerCase();
        b = b.Label.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Type",
    dataIndex: "Type",
    sorter: {
      compare: (a, b) => {
        a = a.Type.toLowerCase();
        b = b.Type.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Default Value",
    dataIndex: "DefaultValue",
    sorter: {
      compare: (a, b) => {
        a = a.DefaultValue.toLowerCase();
        b = b.DefaultValue.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Required",
    dataIndex: "Required",
    sorter: {
      compare: (a, b) => {
        a = a.Required.toLowerCase();
        b = b.Required.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    dataIndex: "Action",
    key: "Action",
    sorter: {
      compare: (a, b) => {
        a = a.Action.toLowerCase();
        b = b.Action.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
]
const data = [
  {
    id: "1",
    Modules: "Plan",
    Label: "Name",
    Type: "Text",
    DefaultValue: "Enter Name",
    Required: "Required",
    Action: "",
  },
  {
    id: "2",
    Modules: "Companies",
    Label: "Email",
    Type: "Email",
    DefaultValue: "Enter Email",
    Required: "Required",
    Action: "",
  },
  {
    id: "3",
    Modules: "Ledger",
    Label: "Phone",
    Type: "Text",
    DefaultValue: "Enter Phone",
    Required: "Required",
    Action: "",
  },
  {
    id: "4",
    Modules: "Packages",
    Label: "Comments",
    Type: "Textarea",
    DefaultValue: "Enter Comments",
    Required: "Required",
    Action: "",
  },
]
export default {
  data() {
    return {
      data,
      columns,
    };
  },
};
</script>
