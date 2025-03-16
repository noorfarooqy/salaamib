<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="card mb-0">
        <div class="card-body">
          <div class="page-header">
            <div class="content-page-header">
              <h5>Edit Products / Services</h5>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group-item">
                <h5 class="form-title">Basic Details</h5>
                <div class="row">
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Item Type<span class="text-danger"> *</span></label>
                      <div class="align-center">
                        <div class="form-control me-3">
                          <label class="custom_radio me-3 mb-0">
                            <input type="radio" class="form-control" name="payment" checked />
                            <span class="checkmark"></span> Product
                          </label>
                        </div>
                        <div class="form-control">
                          <label class="custom_radio mb-0">
                            <input type="radio" name="payment" />
                            <span class="checkmark"></span> Service
                          </label>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="form-group">
                      <label>Product Name <span class="text-danger"> *</span></label>
                      <input type="text" class="form-control" value="" placeholder="Enter Product Name" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="input-block mb-3 add-products">
                      <label>Product Code (SKU)<span class="text-danger"> *</span></label>
                      <input type="text" class="form-control" placeholder="Enter Product Code" />
                      <button type="submit" class="btn btn-primary">
                        Generate Code
                      </button>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Category <span class="text-danger"> *</span></label>
                      <input type="text" class="form-control" value="" placeholder="Enter Category" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Selling Price <span class="text-danger"> *</span></label>
                      <input type="text" class="form-control" value="" placeholder="Enter Selling Price" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Purchase Price <span class="text-danger"> *</span></label>
                      <input type="text" class="form-control" value="" placeholder="Enter Puruchase Price" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Quantity <span class="text-danger"> *</span></label>
                      <input type="number" class="form-control" value="" placeholder="Enter Quantity" name="name" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Units</label>
                      <vue-select :options="Units" id="units" placeholder="Select Units" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Discount Type</label>
                      <vue-select :options="Discount" id="type" placeholder="Select Discount Type" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="input-block mb-3 add-products">
                      <label>Generate Barcode</label>
                      <input type="text" class="form-control" placeholder="Enter Barcode Code" />
                      <button type="submit" class="btn btn-primary">
                        Generate Code
                      </button>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Alert Quantity </label>
                      <input type="number" class="form-control" value="" placeholder="Enter Alert Quantity" name="name" />
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                    <div class="form-group">
                      <label>Tax</label>
                      <vue-select :options="Tax" id="quantity-tax" placeholder="Select Tax" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-group-item">
                <div class="row">
                  <div class="col-xl-6 col-lg-6 col-md-6 col-12 description-box">
                    <div class="form-group" id="summernote_container">
                      <label class="form-control-label">Product Descriptions</label>
                      <editor v-model="content" />
                    </div>
                  </div>
                  <div class="col-xl-6 col-lg-6 col-md-6 col-12">
                    <div class="form-group">
                      <label>Product Image</label>
                      <div class="form-group service-upload mb-0">
                        <span><img src="@/assets/img/icons/drop-icon.svg" alt="upload" /></span>
                        <h6 class="drop-browse align-center">
                          Drop your files here or<span class="text-primary ms-1">browse</span>
                        </h6>
                        <p class="text-muted">Maximum size: 50MB</p>
                        <input type="file" multiple="" id="image_sign" />
                        <div id="frames"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <form @submit.prevent="submitForm" class="text-end">
                <button type="reset" class="btn btn-primary cancel me-2">Cancel</button>
                <button type="submit" class="btn btn-primary">Update</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import Editor from "@tinymce/tinymce-vue";
export default {
  components: {
    editor: Editor,
  },
  data() {
    return {
      content: "Description",
      title: "Edit Products / Services",
      Category: ["Select Item Category", "Category 1", "Category 2", "Category 3"],
      Units: ["Select Units", "Pieces", "Box", "Kilograms"],
      Amount: ["Enter Discount Amount", "5%", "10%", "15%"],
      Discount: ["Select Discount Type", "Percentage", "Fixed"],
      Tax: ["Select Tax", "IVA - (21%)", "IRPF - (-15%)", "PDV - (20%)"],
    };
  },
  methods: {
    submitForm() {
      this.$router.push("/product-list");
    },
  },
  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      const imageSign = document.querySelector("#image_sign");
      imageSign.addEventListener("change", function () {
        const frames = document.querySelector("#frames");
        frames.innerHTML = "";
        for (let i = 0; i < this.files.length; i++) {
          const img = document.createElement("img");
          img.src = window.URL.createObjectURL(this.files[i]);
          img.width = "100";
          img.height = "100";
          frames.appendChild(img);
        }
      });
    });
  },
};
</script>
