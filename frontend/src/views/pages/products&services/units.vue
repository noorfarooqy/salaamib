<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <unitsheader></unitsheader>
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

      <!-- All Invoice -->
      <div class="card invoices-tabs-card">
        <div class="invoices-main-tabs">
          <div class="row align-items-center">
            <div class="col-lg-12">
              <div class="invoices-tabs">
                <ul>
                  <li><router-link to="product-list">Product</router-link></li>
                  <li><router-link to="category">Category</router-link></li>
                  <li><router-link to="units" class="active">Units</router-link></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /All Invoice -->

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'CategoryImage'">
                      <div>{{ record.ShortName }}</div>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_unit"><i class="feather feather-edit"></i></a>
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
    title: "Unit Name",
    dataIndex: "UnitName",
    sorter: {
      compare: (a, b) => {
        a = a.UnitName.toLowerCase();
        b = b.UnitName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Short Name",
    dataIndex: "ShortName",
    key: "ShortName",
    sorter: {
      compare: (a, b) => {
        a = a.ShortName.toLowerCase();
        b = b.ShortName.toLowerCase();
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
    UnitName: "Kilogram",
    ShortName: "kg",
  },
  {
    NUM: "2",
    UnitName: "Gram",
    ShortName: "g",
  },
  {
    NUM: "3",
    UnitName: "Liter",
    ShortName: "l",
  },
  {
    NUM: "4",
    UnitName: "Milliliter",
    ShortName: "ml",
  },
  {
    NUM: "5",
    UnitName: "Pack",
    ShortName: "pk",
  },
  {
    NUM: "6",
    UnitName: "Piece",
    ShortName: "pc",
  },
];

export default {
  data() {
    return {
      Delete: "Delete Units",
      columns,
      data,
    };
  },
};
</script>
