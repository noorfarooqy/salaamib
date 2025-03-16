<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <categoryheader></categoryheader>
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
                  <li>
                    <router-link to="category" class="active">Category</router-link>
                  </li>
                  <li><router-link to="units">Units</router-link></li>
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
                    <template v-if="column.key === 'CategoryName'">
                      <a href="javascript:;" class="product-list-item-img">
                        <img :src="require(`@/assets/img/${record.CategoryImage}`)" alt="product-list" />
                        <span>{{ record.CategoryName }}</span></a>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_category"><i class="feather feather-edit"></i></a>
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
    title: "Category Name",
    dataIndex: "CategoryName",
    key: "CategoryName",
    sorter: {
      compare: (a, b) => {
        a = a.CategoryName.toLowerCase();
        b = b.CategoryName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "TotalProducts",
    dataIndex: "TotalProducts",
    sorter: {
      compare: (a, b) => {
        a = a.TotalProducts.toLowerCase();
        b = b.TotalProducts.toLowerCase();
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
    CategoryName: "Advertising",
    CategoryImage: "product-list-img.jpg",
    TotalProducts: "60",
  },
  {
    NUM: "2",
    CategoryName: "Food",
    CategoryImage: "product-list-img-2.jpg",
    TotalProducts: "55",
  },
  {
    NUM: "3",
    CategoryName: "Furniture",
    CategoryImage: "category-img-03.jpg",
    TotalProducts: "70",
  },
  {
    NUM: "4",
    CategoryName: "Repairs",
    CategoryImage: "category-img-04.jpg",
    TotalProducts: "82",
  },
  {
    NUM: "5",
    CategoryName: "Laptop",
    CategoryImage: "category-img-05.jpg",
    TotalProducts: "26",
  },
  {
    NUM: "6",
    CategoryName: "Shoes",
    CategoryImage: "category-img-06.jpg",
    TotalProducts: "60",
  },
  {
    NUM: "7",
    CategoryName: "Accessories",
    CategoryImage: "category-img-07.jpg",
    TotalProducts: "20",
  },
  {
    NUM: "8",
    CategoryName: "Phone",
    CategoryImage: "category-img-08.jpg",
    TotalProducts: "37",
  },
  {
    NUM: "9",
    CategoryName: "Bages",
    CategoryImage: "category-img-09.jpg",
    TotalProducts: "52",
  },
  {
    NUM: "10",
    CategoryName: "Speaker",
    CategoryImage: "category-img-09.jpg",
    TotalProducts: "156",
  },
];

export default {
  data() {
    return {
      title1: "Delete Category",
      Delete: "Delete Category",
      Parent_Category: ["None", "Coupons", "News", "Plugins", "Themes", "Tutorial"],
      Parent_Category1: ["None", "Coupons", "News", "Plugins", "Themes", "Tutorial"],
      columns,
      data,
    };
  },
};
</script>
