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
              <h5>Edit Customer</h5>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <b-form action="javascript:;">
                <div class="form-group-item">
                  <h5 class="form-title">Basic Details</h5>
                  <div class="profile-picture">
                    <div class="upload-profile">
                      <div class="profile-img">
                        <img id="blah" class="avatar" src="@/assets/img/profiles/avatar-14.jpg" alt="" />
                      </div>
                      <div class="add-profile">
                        <h5>Upload a New Photo</h5>
                        <span>Profile-pic.jpg</span>
                      </div>
                    </div>
                    <div class="img-upload">
                      <label class="btn btn-primary">
                        Upload <input type="file" />
                      </label>
                      <a class="btn btn-remove">Remove</a>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Name</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Name" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Email</label>
                        <b-form-input type="email" class="form-control" placeholder="Enter Email Address" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Phone</label>
                        <vue-tel-input mode="international" class="form-control d-flex" id="phone" name="phone"
                          :defaultCountry="'US'"></vue-tel-input>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Currency</label>
                        <vue-select :options="Currency" placeholder="Select Currency" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Website</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Website Address" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12 mt-3">
                      <div class="form-group">
                        <label>Notes</label>
                        <b-form-input type="email" class="form-control" placeholder="Enter Your Notes" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group-item">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="billing-btn mb-2">
                        <h5 class="form-title">Billing Address</h5>
                      </div>
                      <div class="form-group">
                        <label>Name</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Name" />
                      </div>
                      <div class="form-group mt-3">
                        <label>Address Line 1</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Address 1" />
                      </div>
                      <div class="form-group mt-3">
                        <label>Address Line 2</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Address 1" />
                      </div>
                      <div class="row">
                        <div class="col-lg-6 col-md-12">
                          <div class="form-group mt-3">
                            <label>Country</label>
                            <b-form-input type="text" class="form-control" placeholder="Country" />
                          </div>
                          <div class="form-group mt-3">
                            <label>City</label>
                            <b-form-input type="text" class="form-control" placeholder="City" />
                          </div>
                        </div>
                        <div class="col-lg-6 col-md-12">
                          <div class="form-group mt-3">
                            <label>State</label>
                            <b-form-input type="text" class="form-control" placeholder="State" />
                          </div>
                          <div class="form-group mt-3">
                            <label>Pincode</label>
                            <b-form-input type="text" class="form-control" placeholder="Pincode" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="billing-btn">
                        <h5 class="form-title mb-0">Shipping Address</h5>
                        <a href="javascript:;" class="btn btn-primary">Copy from Billing</a>
                      </div>
                      <div class="form-group">
                        <label>Name</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Name" />
                      </div>
                      <div class="form-group mt-2">
                        <label>Address Line 1</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Address 1" />
                      </div>
                      <div class="form-group mt-3">
                        <label>Address Line 2</label>
                        <b-form-input type="text" class="form-control" placeholder="Enter Address 1" />
                      </div>
                      <div class="row">
                        <div class="col-lg-6 col-md-12">
                          <div class="form-group mt-3">
                            <label>Country</label>
                            <b-form-input type="text" class="form-control" placeholder="Country" />
                          </div>
                          <div class="form-group mt-3">
                            <label>City</label>
                            <b-form-input type="text" class="form-control" placeholder="City" />
                          </div>
                        </div>
                        <div class="col-lg-6 col-md-12">
                          <div class="form-group mt-3">
                            <label>State</label>
                            <b-form-input type="text" class="form-control" placeholder="State" />
                          </div>
                          <div class="form-group mt-3">
                            <label>Pincode</label>
                            <b-form-input type="text" class="form-control" placeholder="Pincode" />
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group-customer customer-additional-form">
                  <div class="row">
                    <h5 class="form-title">Bank Details</h5>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Bank Name</label>
                        <input type="text" class="form-control" placeholder="Enter Bank Name" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="form-group">
                        <label>Branch</label>
                        <input type="text" class="form-control" placeholder="Enter Branch Name" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-12 col-sm-12">
                      <div class="form-group">
                        <label>Account Holder Name</label>
                        <input type="text" class="form-control" placeholder="Enter Account Holder Name" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-12 col-sm-12">
                      <div class="form-group mt-3">
                        <label>Account Number</label>
                        <input type="text" class="form-control" placeholder="Enter Account Number" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-12 col-sm-12">
                      <div class="form-group mt-3">
                        <label>IFSC</label>
                        <input type="text" class="form-control" placeholder="Enter IFSC Code" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="add-customer-btns text-end">
                  <a href="javascript:;" type="reset" class="btn customer-btn-cancel">Cancel</a>
                  <router-link to="/customers/" type="submit" class="btn customer-btn-save">Save Changes</router-link>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["phone"],
  data() {
    return {
      title: "Edit Customers",
      Currency: ["Select Currency", "₹", "$", "£", "€"],
    };
  },
};
</script>
